# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):

    _name = 'on_click.producto'
    _description = 'on_click.producto'

    name = fields.Char()

    currency = fields.Many2one("res.currency", string="Currency")
    price = fields.Monetary(currency_field="currency")
    