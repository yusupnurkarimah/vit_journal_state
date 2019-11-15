# -*- coding: utf-8 -*-
from odoo import http

# class VitJournalState(http.Controller):
#     @http.route('/vit_journal_state/vit_journal_state/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_journal_state/vit_journal_state/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_journal_state.listing', {
#             'root': '/vit_journal_state/vit_journal_state',
#             'objects': http.request.env['vit_journal_state.vit_journal_state'].search([]),
#         })

#     @http.route('/vit_journal_state/vit_journal_state/objects/<model("vit_journal_state.vit_journal_state"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_journal_state.object', {
#             'object': obj
#         })