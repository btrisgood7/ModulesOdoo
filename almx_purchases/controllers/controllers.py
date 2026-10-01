# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxPurchases(http.Controller):
#     @http.route('/almx_purchases/almx_purchases', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_purchases/almx_purchases/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_purchases.listing', {
#             'root': '/almx_purchases/almx_purchases',
#             'objects': http.request.env['almx_purchases.almx_purchases'].search([]),
#         })

#     @http.route('/almx_purchases/almx_purchases/objects/<model("almx_purchases.almx_purchases"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_purchases.object', {
#             'object': obj
#         })
