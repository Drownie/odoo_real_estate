from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

class DroRsPropertyTransaction(models.Model):
    _name = 'dro.rs.property.transaction'
    _description = 'Transaction'

    # Extend Methods
    @api.model
    def _read_group_state_ids(self, stages, domain, order):
        _logger.info("LOG: %s", self.env['dro.rs.property.transaction.state'].search([]).ids)

        # return stages.search([('id', 'in', stages.ids)])
        return self.env['dro.rs.property.transaction.state'].search([])
    
    @api.model
    def write(self, vals):
        res = super(DroRsPropertyTransaction, self).write(vals)

        # Convert the partner into property client
        for rec in self:
            if 'client_id' in vals:
                if not rec.client_id.is_property_client:
                    rec.client_id.is_property_client = True

        return res
    
    # Compute methods
    def _compute_currency_id(self):
        main_company = self.env['res.company']._get_main_company()
        for template in self:
            template.currency_id = main_company.currency_id.id

    # Onchange methods
    @api.onchange('property_id')
    def _onchange_property(self):
        if self.property_id:
            if self.commission_type == 'fixed':
                self.nego_price = self.price + self.commission_amount
            else:
                self.nego_price = self.price

    currency_id = fields.Many2one('res.currency', 'Currency', compute='_compute_currency_id')

    name = fields.Char('Title')
    
    client_id = fields.Many2one('res.partner', required=True)

    client_phone = fields.Char(related='client_id.phone')

    client_email = fields.Char(related='client_id.email')

    state_id = fields.Many2one('dro.rs.property.transaction.state', group_expand="_read_group_state_ids", required=True)

    property_id = fields.Many2one('dro.rs.property', 'Property')

    property_availability = fields.Selection(related='property_id.availability_type')

    property_type = fields.Many2one(related='property_id.property_type')

    landlord_id = fields.Many2one(related='property_id.landlord_id')

    landlord_email = fields.Char(related='property_id.landlord_email')
    
    landlord_phone = fields.Char(related='property_id.landlord_phone')

    negotiable = fields.Boolean(related='property_id.negotiable')

    price = fields.Monetary(related='property_id.price')

    commission_type = fields.Selection(related='property_id.commission_type', store=True, readonly=False)

    commission_percentage = fields.Float(related='property_id.commission_percentage', store=True, readonly=False)

    commission_amount = fields.Monetary(related='property_id.commission_amount', store=True, readonly=False)

    nego_price = fields.Monetary('Nego Price', 'currency_id')

    activity_state = fields.Selection([('planned', 'Planned')], string='Activity State', default='planned')