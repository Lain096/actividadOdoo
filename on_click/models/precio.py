# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Precio(models.Model):

    _inherit = 'on_click.producto'
    '''
    _name = 'on_click.precio'
    _description = 'Variantes de precio para cada producto dependiendo del lugar en el que se celebre'
    '''

    currency = fields.Many2one("res.currency", string="Currency")

    place = fields.Many2one(comodel_name="on_click.lugar", string="Lugar")
    extra = fields.Monetary(currency_field="currency", string="Aumento")
    total = fields.Monetary(currency_field="currency", string="Total", readonly=True)

    @api.onchange('price', 'extra')
    def _calcular_total(self):
        self.total = self.price + self.extra