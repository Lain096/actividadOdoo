# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Contrato(models.Model):
    _name = 'on_click.contrato'
    _description = 'Contrato generado a partir de todo lo variado en los demas modelos'


    name = fields.Char(string="Nombre del comtrato")

    client = fields.Many2one(comodel_name="on_click.cliente", string ="Información del cliente")
    organizer = fields.Many2one(comodel_name="on_click.organizador", string="Información del organizador")

    product = fields.Many2many(comodel_name="on_click.producto", inverse_name='contrato', string="Productos contratados")
    event = fields.Many2one(comodel_name="on_click.evento", string="Información del evento a realizar")

    @api.constrains('event')
    def _check_max_events(self):
        for record in self:
                if len(record.event) > 2:
                    raise exceptions.ValidationError("No puedes tener más de 1 evento en un contrato")