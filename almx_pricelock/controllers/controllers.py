# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxPricelock(http.Controller):
#     @http.route('/almx_pricelock/almx_pricelock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_pricelock/almx_pricelock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_pricelock.listing', {
#             'root': '/almx_pricelock/almx_pricelock',
#             'objects': http.request.env['almx_pricelock.almx_pricelock'].search([]),
#         })

#     @http.route('/almx_pricelock/almx_pricelock/objects/<model("almx_pricelock.almx_pricelock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_pricelock.object', {
#             'object': obj
#         })
