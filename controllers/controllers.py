# -*- coding: utf-8 -*-
# from odoo import http


# class /odoo/c-addons/demo(http.Controller):
#     @http.route('//odoo/c-addons/demo//odoo/c-addons/demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/c-addons/demo//odoo/c-addons/demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/c-addons/demo.listing', {
#             'root': '//odoo/c-addons/demo//odoo/c-addons/demo',
#             'objects': http.request.env['/odoo/c-addons/demo./odoo/c-addons/demo'].search([]),
#         })

#     @http.route('//odoo/c-addons/demo//odoo/c-addons/demo/objects/<model("/odoo/c-addons/demo./odoo/c-addons/demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/c-addons/demo.object', {
#             'object': obj
#         })
