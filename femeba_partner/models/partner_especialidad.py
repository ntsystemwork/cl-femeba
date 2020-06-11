# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PartnerEspecialidad(models.Model):
    _name = 'res.partner.especialidad'
    name = fields.Char('Descripcion', required = False)