# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxReportTemplates(http.Controller):
#     @http.route('/almx_report_templates/almx_report_templates', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_report_templates/almx_report_templates/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_report_templates.listing', {
#             'root': '/almx_report_templates/almx_report_templates',
#             'objects': http.request.env['almx_report_templates.almx_report_templates'].search([]),
#         })

#     @http.route('/almx_report_templates/almx_report_templates/objects/<model("almx_report_templates.almx_report_templates"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_report_templates.object', {
#             'object': obj
#         })
