from odoo import models, fields

class DroRsPropertySpec(models.Model):
    _name = 'dro.rs.property.spec'
    _description = 'List every real estate specifications'

    name = fields.Char('Nama', related='facility_id.display_name')

    facility_id = fields.Many2one('dro.rs.property.facility', 'Facility')

    quantity = fields.Integer('Qty')

    real_estate_id = fields.Many2one('dro.rs.property', 'Real estate')