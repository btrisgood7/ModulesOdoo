# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class almx_csf(models.Model):
#     _name = 'almx_csf.almx_csf'
#     _description = 'almx_csf.almx_csf'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
