# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class almx_report_templates(models.Model):
#     _name = 'almx_report_templates.almx_report_templates'
#     _description = 'almx_report_templates.almx_report_templates'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
