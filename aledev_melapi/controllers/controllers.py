# -*- coding: utf-8 -*-
# from odoo import http


# class AledevMelapi(http.Controller):
#     @http.route('/aledev_melapi/aledev_melapi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aledev_melapi/aledev_melapi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aledev_melapi.listing', {
#             'root': '/aledev_melapi/aledev_melapi',
#             'objects': http.request.env['aledev_melapi.aledev_melapi'].search([]),
#         })

#     @http.route('/aledev_melapi/aledev_melapi/objects/<model("aledev_melapi.aledev_melapi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aledev_melapi.object', {
#             'object': obj
#         })
