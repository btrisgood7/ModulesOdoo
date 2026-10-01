from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    apply_points = fields.Boolean(compute='compute_apply_points', string='¿Aplicar puntos?')

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            partner = order.partner_id
            total = order.amount_total or 0.0
            points = int(total // 8)  # 1 punto por cada 8 pesos

            if points > 0 and partner:
                # leemos los puntos actuales
                current_points = partner.loyalty_points or 0
                # escribimos con sudo por permisos
                partner.sudo().write({
                    'loyalty_points': current_points + points
                })
        return res