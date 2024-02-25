# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lugar(models.Model):
    _name = 'on_click.lugar'
    _description = 'Lugares idílicos para celebrar cosas'

    name = fields.Char(string="Nombre")
    place = fields.Char(string="Localización")
    max_people = fields.Integer(string="Número máximo de asistentes")
    image = fields.Image(string="Imagen del lugar")
    description = fields.Text(string="Descripción del lugar")
    price = fields.Float(string="Alquiler por día")