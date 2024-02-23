# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Organizador(models.Model):
    _name = 'on_click.organizador'
    _description = 'Un organizador de eventos'
    _inherit = 'on_click.persona'

    profile = fields.Binary(string="Image")
    roles = fields.Text(string="Roles")