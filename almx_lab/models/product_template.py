from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product' #Herencia del módelo producto

    verification_lab = fields.Boolean(string='Producto Programable', help='Verifica si producto es programable por el equipo de Laboratorio')
    stock_it = fields.Boolean(String='Equipo de IT', help='Verifica si producto es equipo de cómputo/IT')
    lab_task = fields.One2many(comodel_name='lab.task', inverse_name="product_id", string='Productos Programables')