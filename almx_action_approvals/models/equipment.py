from odoo import models, fields, api

#Aquí se declara el one2many que aparecerá en aprovaciones
class Equipment(models.Model):
    _name = 'equipment.compute'
    _description = 'Equipo de computo'

    id = fields.Integer(string='id')
    name_product = fields.Many2one('product.product', string='Nombre del equipo', readonly=True)
    sku_product = fields.Many2one('product.product', string='Número de serie', readonly=True)
    quant_product = fields.Integer('product.product', string='Cantidad del serie', readonly=True)




