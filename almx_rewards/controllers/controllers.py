# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxRewards(http.Controller):
#     @http.route('/almx_rewards/almx_rewards', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_rewards/almx_rewards/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_rewards.listing', {
#             'root': '/almx_rewards/almx_rewards',
#             'objects': http.request.env['almx_rewards.almx_rewards'].search([]),
#         })

#     @http.route('/almx_rewards/almx_rewards/objects/<model("almx_rewards.almx_rewards"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_rewards.object', {
#             'object': obj
#         })
