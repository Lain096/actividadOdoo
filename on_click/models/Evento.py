# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Evento(models.Model):
    _name = 'on_click.evento'
    _description = 'Eventos que se pueden organizar y donde pueden tener lugar'

    name = fields.Char(string="Nombre del evento")
    place = fields.Many2one(comodel_name="on_click.lugar" , string="Lugar del Evento")
    max_people = fields.Integer(string="Número Máximo de Asistentes", related="place.max_people")
    image = fields.Image(related="place.image")
    date_start = fields.Date(string="Fecha de Inicio", required=True)
    date_end = fields.Date(string="Fecha de Fin", required=True)
    description = fields.Text(string="Descripción del Evento")
    price = fields.Float(string="Coste", compute='_compute_event_price', store=True)

    #Constraints el castillo de las olas sólo puede ser reservado 1 vez para las fechas X e Y

    @api.depends('date_start', 'date_end', 'place.price')
    def _compute_event_price(self):
        for event in self:
            if event.date_start and event.date_end:

                duration = (event.date_end - event.date_start).days + 1

                event.price = duration * event.place.price
            else:
                event.price = 0.0

    @api.constrains('place', 'date_start', 'date_end')
    def _check_reservation_availability(self):
        for event in self:
            if event.place and event.date_start and event.date_end:
                # Verificar si hay eventos superpuestos en el mismo lugar
                overlapping_events = self.env['on_click.evento'].search([
                    ('place', '=', event.place.id),
                    ('date_start', '<=', event.date_end),
                    ('date_end', '>=', event.date_start),
                    ('id', '!=', event.id),
                ])
                if overlapping_events:
                    raise ValidationError("Este lugar ya está reservado para las fechas seleccionadas.")

