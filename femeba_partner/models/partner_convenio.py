# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PartnerConvenio(models.Model):
    _name = 'res.partner.convenio'
    name = fields.Char('Descripcion', required = False)