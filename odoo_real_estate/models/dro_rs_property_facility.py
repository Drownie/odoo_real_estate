from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DroRsPropertyFacility(models.Model):
    _name = 'dro.rs.property.facility'
    _description = 'Real Estate Facility'

    _sql_constraints = [
        ('unique_name', 'UNIQUE (LOWER(name))', 'The name must be unique!')
    ]

    # Constraint methods
    @api.constrains('name')
    def _check_unique_name(self):
        for rec in self:
            if self.env['dro.rs.property.facility'].search_count([('name', '=', rec.name), ('id', '!=', rec.id)]) > 0:
                raise ValidationError('The name must be unique!')

    name = fields.Char(string="Name", required=True)
