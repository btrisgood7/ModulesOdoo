# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxActionApprovals(http.Controller):
#     @http.route('/almx_action_approvals/almx_action_approvals', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_action_approvals/almx_action_approvals/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_action_approvals.listing', {
#             'root': '/almx_action_approvals/almx_action_approvals',
#             'objects': http.request.env['almx_action_approvals.almx_action_approvals'].search([]),
#         })

#     @http.route('/almx_action_approvals/almx_action_approvals/objects/<model("almx_action_approvals.almx_action_approvals"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_action_approvals.object', {
#             'object': obj
#         })
