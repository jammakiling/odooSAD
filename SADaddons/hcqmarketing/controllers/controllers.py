# -*- coding: utf-8 -*-
# from odoo import http


# class Sadaddons/hcqmarketing(http.Controller):
#     @http.route('/sadaddons/hcqmarketing/sadaddons/hcqmarketing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sadaddons/hcqmarketing/sadaddons/hcqmarketing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sadaddons/hcqmarketing.listing', {
#             'root': '/sadaddons/hcqmarketing/sadaddons/hcqmarketing',
#             'objects': http.request.env['sadaddons/hcqmarketing.sadaddons/hcqmarketing'].search([]),
#         })

#     @http.route('/sadaddons/hcqmarketing/sadaddons/hcqmarketing/objects/<model("sadaddons/hcqmarketing.sadaddons/hcqmarketing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sadaddons/hcqmarketing.object', {
#             'object': obj
#         })

