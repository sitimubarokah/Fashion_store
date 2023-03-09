# -*- coding: utf-8 -*-
# from odoo import http


# class FashionStore(http.Controller):
#     @http.route('/fashion__store/fashion__store/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fashion__store/fashion__store/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fashion__store.listing', {
#             'root': '/fashion__store/fashion__store',
#             'objects': http.request.env['fashion__store.fashion__store'].search([]),
#         })

#     @http.route('/fashion__store/fashion__store/objects/<model("fashion__store.fashion__store"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fashion__store.object', {
#             'object': obj
#         })
