# -*- coding: utf-8 -*-
from odoo import http

# class TestQuadi(http.Controller):
#     @http.route('/test_quadi/test_quadi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_quadi/test_quadi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_quadi.listing', {
#             'root': '/test_quadi/test_quadi',
#             'objects': http.request.env['test_quadi.test_quadi'].search([]),
#         })

#     @http.route('/test_quadi/test_quadi/objects/<model("test_quadi.test_quadi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_quadi.object', {
#             'object': obj
#         })