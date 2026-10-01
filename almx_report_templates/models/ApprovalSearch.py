from odoo import models, fields, api
from odoo.exceptions import UserError

class Approval(models.Model):
    _inherit = "approval.request"

    approval_loan = fields.One2many('approval.loan', 'request_id',                    # <- inverso
        string='Préstamo de equipo de cómputo', readonly=True)

    @api.model
    def create(self, vals):
        record = super(Approval, self).create(vals)

        employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1)
        if not (employee and employee.stock_location_id):
            return record

        loc = employee.stock_location_id
        Quant = self.env['stock.quant']
        quants = Quant.search([
            ('location_id', 'child_of', loc.id),
            ('quantity', '>', 0),
        ])

        loan_lines_vals = []
        for q in quants:
            product = q.product_id
            if not product:
                continue

            # --- 3) Solo laptops y cargadores ---
            if not (product.is_laptop or product.is_cargador):
                continue

            # Hace una decisión dependiendo si es: Laptop / Cargador ---
            if product.is_laptop:
                category = "Laptop"
            elif product.is_cargador:
                category = "Cargador"
            else:
                category = ""  # fallback, no debería ocurrir por el filtro de arriba

            # Nombre del producto asignado ---
            product_name = product.display_name or product.name or ''

            serial = q.lot_id.name if q.lot_id else ''

            loan_lines_vals.append((0, 0, {
                'category_id': category,  # texto visible
                'model_id': product_name,  # aquí va el nombre del producto
                'serial_number': serial,
            }))

        if loan_lines_vals:
            record.approval_loan = loan_lines_vals

        return record


class ProductProduct(models.Model):
    _inherit = 'product.product'

    stock_it = fields.Boolean(string='Equipo de IT', help='Verifica si producto es equipo de cómputo/IT')
    is_laptop = fields.Boolean(string='¿Es laptop?', help='Verifica si es una laptop')
    is_cargador = fields.Boolean(string='¿Es cargador?', help='Verifica si es cargador')



