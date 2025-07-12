from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

# Constant
STATE = [
    ('draft', 'Draft'),
    ('posted', 'Posted'),
]

class DroRsProperty(models.Model):
    _name = 'dro.rs.property'
    _description = 'Property Item'

    # Action Methods
    def action_set_draft(self):
        self.state = 'draft'

    def action_set_posted(self):
        if not self.landlord_id:
            raise ValidationError("Please set the landlord")
        
        self.state = 'posted'

    # Extend Methods
    @api.model
    def _group_expand_state(self, stages, domain: list[list], order):
        _logger.info("DOMAIN = %s", domain)
        include_states = set()  # States explicitly included
        exclude_states = set()  # States to exclude

        for condition in domain:
            if isinstance(condition, (list, tuple)) and len(condition) >= 3:
                field, operator, value = condition[:3]
                if field == 'state':
                    if operator in ('in', '='):  # Include states
                        if isinstance(value, list):
                            include_states.update(value)
                        elif isinstance(value, str):
                            include_states.add(value)
                    elif operator in ('not in', '!='):  # Exclude states
                        if isinstance(value, list):
                            exclude_states.update(value)
                        elif isinstance(value, str):
                            exclude_states.add(value)

        # Get all possible states from STATE_SELECTION in order
        all_states = [state[0] for state in STATE]

        # If there's an inclusion filter, use it, otherwise use all states
        state_values = include_states if include_states else set(all_states)

        # Apply exclusion filter
        filtered_states = [state for state in all_states if state in state_values and state not in exclude_states]

        return filtered_states

    # Compute methods
    def _compute_currency_id(self):
        main_company = self.env['res.company']._get_main_company()
        for template in self:
            template.currency_id = main_company.currency_id.id
        
    @api.onchange('commission_percentage')
    def _compute_commission_amount(self):
        if self.commission_type == 'percentage':
            self.commission_amount = (self.commission_percentage / 100) * self.price

    currency_id = fields.Many2one('res.currency', 'Currency', compute='_compute_currency_id')

    name = fields.Char('Title', help="Title", required=True)

    address = fields.Text('Address')

    zip = fields.Char(change_default=True)
    
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    
    country_code = fields.Char(related='country_id.code', string="Country Code")

    price = fields.Monetary('Price', 'currency_id')

    total_area = fields.Integer('Total Area')

    building_area = fields.Integer('Building Area')

    agent_id = fields.Many2one('res.users', 'Agent', default=lambda self: self.env.user.id)

    spec_ids = fields.One2many('dro.rs.property.spec', 'real_estate_id', 'Specifications')

    descriptions = fields.Html('Descriptions')

    property_type = fields.Many2one('dro.rs.property.type', 'Property Type')

    negotiable = fields.Boolean('Negotiable?')

    availability_type = fields.Selection([
        ('rent', 'Rent'),
        ('sell', 'Sell'),
        ('both', 'Both'),
    ], default='rent', string='Availability Type', required=True)

    rent_payment_term = fields.Selection([
        ('day', 'Daily'),
        ('week', 'Weekly'),
        ('month', 'Monthly'),
        ('year', 'Yearly'),
    ], 'Payment Terms', default='year')

    rent_security_deposit = fields.Monetary('Deposits', 'currency_id')

    landlord_id = fields.Many2one('res.partner', 'Owner')

    landlord_email = fields.Char('Email', related='landlord_id.email')

    landlord_phone = fields.Char('Phone', related='landlord_id.phone')

    state = fields.Selection(STATE, 'Status', default='draft', group_expand="_group_expand_state")

    is_active = fields.Boolean('Active?', default=False)

    activity_state = fields.Selection([
        ('overdue', 'Overdue'),
        ('today', 'Today'),
        ('planned', 'Planned')],
        string='Activity State',
        default='planned')
    
    # Commission Setting

    commission_type = fields.Selection([
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed')
    ], default='fixed', string='Commission Type')

    commission_amount = fields.Monetary('Commission Amount', 'currency_id')

    commission_percentage = fields.Float('Commission Percentage(%)', default=0)

    # Tenant Management

    