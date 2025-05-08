from odoo import models, fields, api

class Client(models.Model):
    _name = 'dro.rs.property.client'
    # _inherit = 'res.partner'
    _description = 'Client'

    # Extend Methods
    
    @api.model
    def _name_search(self, name: str, domain: list | None =None, operator='ilike', limit=None, order=None):
        domain = domain or []
        if name:
            domain = ['|', '|',
                ('name', operator, name),
                ('phone', operator, name),
                ('mobile', operator, name)] + domain
        
        return self._search(domain, limit=limit, order=order)
    
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')

    name = fields.Char(related='partner_id.name', store=True, readonly=False)

    phone = fields.Char(related='partner_id.phone', store=True, readonly=False)
    
    email = fields.Char(related='partner_id.email', store=True, readonly=False)

    avatar_1920 = fields.Image("Avatar", related='partner_id.avatar_128', store=True, readonly=False)

    avatar_1024 = fields.Image("Avatar 1024", related='partner_id.avatar_128', store=True, readonly=False)

    avatar_512 = fields.Image("Avatar 512", related='partner_id.avatar_128', store=True, readonly=False)
    
    avatar_256 = fields.Image("Avatar 256", related='partner_id.avatar_128', store=True, readonly=False)
    
    avatar_128 = fields.Image("Avatar 128", related='partner_id.avatar_128', store=True, readonly=False)

    image_1920 = fields.Image(related='partner_id.image_1920', store=True, readonly=False)

    rating = fields.Integer('Rating')

    special_note = fields.Text('Special Note')