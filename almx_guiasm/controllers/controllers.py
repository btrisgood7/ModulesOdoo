# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxGuiasm(http.Controller):
#     @http.route('/almx_guiasm/almx_guiasm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_guiasm/almx_guiasm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_guiasm.listing', {
#             'root': '/almx_guiasm/almx_guiasm',
#             'objects': http.request.env['almx_guiasm.almx_guiasm'].search([]),
#         })

#     @http.route('/almx_guiasm/almx_guiasm/objects/<model("almx_guiasm.almx_guiasm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_guiasm.object', {
#             'object': obj
#         })
