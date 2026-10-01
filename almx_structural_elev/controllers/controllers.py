# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxStructuralElev(http.Controller):
#     @http.route('/almx_structural_elev/almx_structural_elev', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_structural_elev/almx_structural_elev/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_structural_elev.listing', {
#             'root': '/almx_structural_elev/almx_structural_elev',
#             'objects': http.request.env['almx_structural_elev.almx_structural_elev'].search([]),
#         })

#     @http.route('/almx_structural_elev/almx_structural_elev/objects/<model("almx_structural_elev.almx_structural_elev"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_structural_elev.object', {
#             'object': obj
#         })
