# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Evento(models.Model):
    _inherit = 'on_click.evento'

    state = fields.Selection([("I", "Incompleto"), ("P", "Preparado"), ("T", "Terminado")], compute="_compute_estado", string="Estado", default="I")

    # Si la fecha de fin es anterior a la actual, el estado del evento será terminado
    @api.depends('date_end')
    def _compute_estado(self):
        for record in self:
            if record.date_end and record.date_end < fields.Date.today():
                record.state = "T"
            else:
                record.state = "I"