# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PartnerCargo(models.Model):
    _name = 'res.partner.cargo'
    name = fields.Char('Descripcion', required = False)