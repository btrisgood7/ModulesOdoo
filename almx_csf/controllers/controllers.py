# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxCsf(http.Controller):
#     @http.route('/almx_csf/almx_csf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_csf/almx_csf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_csf.listing', {
#             'root': '/almx_csf/almx_csf',
#             'objects': http.request.env['almx_csf.almx_csf'].search([]),
#         })

#     @http.route('/almx_csf/almx_csf/objects/<model("almx_csf.almx_csf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_csf.object', {
#             'object': obj
#         })
