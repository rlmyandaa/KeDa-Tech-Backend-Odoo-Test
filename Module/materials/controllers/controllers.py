# -*- coding: utf-8 -*-
# from odoo import http


# class Materials(http.Controller):
#     @http.route('/materials/materials/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/materials/materials/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('materials.listing', {
#             'root': '/materials/materials',
#             'objects': http.request.env['materials.materials'].search([]),
#         })

#     @http.route('/materials/materials/objects/<model("materials.materials"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('materials.object', {
#             'object': obj
#         })
