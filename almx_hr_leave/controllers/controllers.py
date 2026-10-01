# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxHrLeave(http.Controller):
#     @http.route('/almx_hr_leave/almx_hr_leave', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_hr_leave/almx_hr_leave/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_hr_leave.listing', {
#             'root': '/almx_hr_leave/almx_hr_leave',
#             'objects': http.request.env['almx_hr_leave.almx_hr_leave'].search([]),
#         })

#     @http.route('/almx_hr_leave/almx_hr_leave/objects/<model("almx_hr_leave.almx_hr_leave"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_hr_leave.object', {
#             'object': obj
#         })
