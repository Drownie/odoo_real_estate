from odoo import models, fields, api

class DroRsPropertyTransactionState(models.Model):
    _name = 'dro.rs.property.transaction.state'
    _description = 'Transaction State'

    # Extend Methods

    name = fields.Char('Title')

    sequence = fields.Integer(default=1, string="Sequence")

    fold = fields.Boolean(string='Folded?')