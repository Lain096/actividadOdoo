# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):
    _name = 'on_click.producto'
    _description = 'Los productos que se ofrecen en los eventos'

    name = fields.Char(string="Producto")
    quantity = fields.Integer(string = "Cantidad disponible")
    price = fields.Float(string="Precio del producto")
    image = fields.Image(string="Imagen del producto")
    description = fields.Char(string="Descripcion del producto") 
    contrato = fields.Many2many(comodel_name="on_click.contrato", string="Contrato")



