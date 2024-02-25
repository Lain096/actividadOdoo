# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import datetime
import re


class Persona(models.Model):
    _name = 'on_click.persona'
    _description = 'Esqueleto de persona'

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Correo Electrónico")
    tel = fields.Char(string="Teléfono")
    dni = fields.Char(string="DNI", required=True)
    birthdate = fields.Date(string="Fecha de nacimiento")
    address = fields.Char(string="Dirección")
    is_adult = fields.Boolean(compute='_compute_mayor_de_edad', store=True)


    # DNI único
    _sql_constraints = [
    	('dni_unique', 'UNIQUE(dni)', 'El cliente ya existe')
    ]

    # El DNI debe ser válido para poder agregar el cliente, 9 dígitos y letra correcta según la tabla
    @api.constrains('dni')
    def _check_dni_correcto(self):
        for record in self:
            if record.dni:
                if len(record.dni) != 9:
                    raise ValidationError("El DNI debe tener 9 dígitos")
                try:
                    int(record.dni[:-1])
                except ValueError:
                    raise ValidationError("El DNI no es válido")
                letra = record.dni[-1]
                letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
                if letra.upper() != letras[int(record.dni[:-1]) % 23]:
                    raise ValidationError("La letra del DNI no es válida")

    # El email debe tener un formato correcto, con el uso del arroba y punto
    @api.constrains('email')
    def _check_email_formato(self):
        for record in self:
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError("El correo electrónico no es válido")

    # Se debe introducir al menos un correo o un telefono
    @api.constrains('email', 'tel')
    def _check_contacto(self):
        for record in self:
            if record.email:
                pass
            elif record.tel:
                pass
            else:
                raise ValidationError("Debe haber al menos un método de contacto (Teléfono/Correo electrónico)")

    # Si es mayor de edad
    @api.depends('birthdate')
    def _compute_mayor_de_edad(self):
        if self.birthdate:
            d1 = self.birthdate
            d2 = datetime.date.today()
            age = relativedelta(d2, d1).years
            self.is_adult = age >=18
