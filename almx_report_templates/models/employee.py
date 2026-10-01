from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Este es el campo clave que necesitamos
    # Relaciona al empleado con UNA ubicación de inventario
    stock_location_id = fields.Many2one(
        'stock.location',
        string='Ubicación de Stock de IT',
        domain="[('usage', '=', 'internal')]",
        help="Ubicación interna donde se almacena el equipo de IT asignado a este empleado."
    )