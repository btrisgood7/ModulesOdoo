# models/res_partner.py
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_points = fields.Integer(string='Puntos de lealtad', default=0)
