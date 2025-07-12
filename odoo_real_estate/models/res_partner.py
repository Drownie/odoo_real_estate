from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_property_client = fields.Boolean(default=False)

    rating = fields.Integer('Rating', default=0)