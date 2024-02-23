# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contrato(models.Model):

    _name = 'on_click.contrato'
    _description = 'on_click.contrato'

    name = fields.Char()
    client = fields.Many2one(comodel_name="on_click.cliente")
    #product = fields.Many2many(comodel_name="on_click.producto", string="Producto")
    #event = fields.Char()
    