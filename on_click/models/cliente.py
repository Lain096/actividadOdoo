# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'on_click.cliente'
    _description = 'Un cliente de la empresa'
    _inherit = 'on_click.persona'


    history = fields.One2many(comodel_name="on_click.contrato", inverse_name="client", string="Contrato")


