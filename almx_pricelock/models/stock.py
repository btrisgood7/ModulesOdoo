from odoo import models, fields, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    list_price = fields.Float(tracking=True)

    def write(self, vals):
        if 'list_price' in vals and not self.env.user.has_group('almx_pricelock.group_edit_sale_price'):
            raise UserError(_("No tienes permiso para modificar el Precio de venta."))
        return super().write(vals)

