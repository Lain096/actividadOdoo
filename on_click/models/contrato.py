# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


class Contrato(models.Model):
    _name = 'on_click.contrato'
    _description = 'Contrato generado a partir de todo lo variado en los demas modelos'


    name = fields.Char(string="Nombre del comtrato")

    client = fields.Many2one(comodel_name="on_click.cliente", string ="Cliente")
    organizer = fields.Many2many(comodel_name="on_click.organizador", string="Organizador")

    product = fields.Many2many(comodel_name="on_click.producto", inverse_name='contrato', string="Productos contratados")
    event = fields.Many2one(comodel_name="on_click.evento", string="Evento")


    price = fields.Float(string="Precio total", compute="_compute_price", store=True)

    @api.constrains('event')
    def _check_max_events(self):
        for record in self:
                if len(record.event) > 2:
                    raise exceptions.ValidationError("No puedes tener más de 1 evento en un contrato")

    @api.depends('product', 'event')
    def _compute_price(self):
        for record in self:
            product_price = sum(record.product.mapped('price'))
            event_price = record.event.price
            total_price = product_price + event_price
            record.price = total_price

