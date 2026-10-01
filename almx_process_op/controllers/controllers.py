# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxProcessOp(http.Controller):
#     @http.route('/almx_process_op/almx_process_op', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_process_op/almx_process_op/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_process_op.listing', {
#             'root': '/almx_process_op/almx_process_op',
#             'objects': http.request.env['almx_process_op.almx_process_op'].search([]),
#         })

#     @http.route('/almx_process_op/almx_process_op/objects/<model("almx_process_op.almx_process_op"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_process_op.object', {
#             'object': obj
#         })
