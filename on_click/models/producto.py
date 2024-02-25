# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):
    _name = 'on_click.producto'
    _description = 'Los productos que se ofrecen en los eventos'

    name = fields.Char(string="Producto", required=True)
    quantity = fields.Integer(string = "Cantidad disponible")
    price = fields.Float(string="Precio del producto", required=True)
    image = fields.Image(string="Imagen del producto")
    description = fields.Char(string="Descripcion del producto") 
    contrato = fields.Many2many(comodel_name="on_click.contrato", string="Contrato")

    variants = fields.One2many(comodel_name="on_click.variantes", inverse_name="product")


class Variantes(models.Model):
    _name = 'on_click.variantes'
    _description = 'Variantes de un producto específico'

    product = fields.Many2one(comodel_name="on_click.producto")
    attribute = fields.Char(String="Atributo")
    value = fields.Many2many(comodel_name="on_click.valores", string="Valores")


class Valores(models.Model):
    _name = 'on_click.valores'
    _description = 'Valores para cada atributo'

    name = fields.Char(string="valor", required=True)