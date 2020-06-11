# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PartnerEntidad(models.Model):
    _name = 'res.partner.entidad'
    name = fields.Char('Descripcion', required = False)