from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product' #Herencia del módelo producto

    verification_lab = fields.Boolean(string='Producto Programable', help='Verifica si producto es programable por el equipo de Laboratorio')
    lab_task = fields.One2many(comodel_name='lab.task', inverse_name="product_id", string='Productos Programables')