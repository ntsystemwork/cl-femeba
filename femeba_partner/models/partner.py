# -*- coding: utf-8 -*-
from odoo import models, fields

class Partner(models.Model):
    _inherit ='res.partner'
    _name = 'res.partner'
    professional_registration = fields.Char('Matricula Profesional', required = False)
    cargo_id = fields.Many2one('res.partner.cargo','Cargo') 
    especialidad_id = fields.Many2one('res.partner.especialidad','Especialidad') 
    university = fields.Char('Universidad', required = False)
    organization = fields.Char('Organización', required = False)
    entidad_id = fields.Many2one('res.partner.entidad','Entidad primaria') 
    convenio_id = fields.Many2one('res.partner.convenio','Convenio') 
