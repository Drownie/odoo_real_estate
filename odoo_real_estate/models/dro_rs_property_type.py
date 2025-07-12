from odoo import models, fields

class DroRsPropertyType(models.Model):
    _name = 'dro.rs.property.type'
    _description = 'Property Type'

    name = fields.Char('Type Name')