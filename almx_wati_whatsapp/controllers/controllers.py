# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxWatiWhatsapp(http.Controller):
#     @http.route('/almx_wati_whatsapp/almx_wati_whatsapp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_wati_whatsapp/almx_wati_whatsapp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_wati_whatsapp.listing', {
#             'root': '/almx_wati_whatsapp/almx_wati_whatsapp',
#             'objects': http.request.env['almx_wati_whatsapp.almx_wati_whatsapp'].search([]),
#         })

#     @http.route('/almx_wati_whatsapp/almx_wati_whatsapp/objects/<model("almx_wati_whatsapp.almx_wati_whatsapp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_wati_whatsapp.object', {
#             'object': obj
#         })
