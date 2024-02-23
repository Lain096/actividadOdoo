# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lugar(models.Model):

    _name = 'on_click.lugar'
    _description = 'on_click.lugar'
    
    name = fields.Char()
    