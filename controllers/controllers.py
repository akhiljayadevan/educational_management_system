# -*- coding: utf-8 -*-
# from odoo import http


# class EducationalManagementSystem(http.Controller):
#     @http.route('/educational_management_system/educational_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/educational_management_system/educational_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('educational_management_system.listing', {
#             'root': '/educational_management_system/educational_management_system',
#             'objects': http.request.env['educational_management_system.educational_management_system'].search([]),
#         })

#     @http.route('/educational_management_system/educational_management_system/objects/<model("educational_management_system.educational_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('educational_management_system.object', {
#             'object': obj
#         })
