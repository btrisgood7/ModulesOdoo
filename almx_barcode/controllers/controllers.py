# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxBarcode(http.Controller):
#     @http.route('/almx_barcode/almx_barcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_barcode/almx_barcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_barcode.listing', {
#             'root': '/almx_barcode/almx_barcode',
#             'objects': http.request.env['almx_barcode.almx_barcode'].search([]),
#         })

#     @http.route('/almx_barcode/almx_barcode/objects/<model("almx_barcode.almx_barcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_barcode.object', {
#             'object': obj
#         })
