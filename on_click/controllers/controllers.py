# -*- coding: utf-8 -*-
# from odoo import http


# class OnClick(http.Controller):
#     @http.route('/on_click/on_click', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/on_click/on_click/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('on_click.listing', {
#             'root': '/on_click/on_click',
#             'objects': http.request.env['on_click.on_click'].search([]),
#         })

#     @http.route('/on_click/on_click/objects/<model("on_click.on_click"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('on_click.object', {
#             'object': obj
#         })

