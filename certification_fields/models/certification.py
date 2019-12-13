from odoo import api, fields, models

class Certification(models.Model):
    _inherit = "event.event"

    programa = fields.Text(string='Programa')

    cantidad_horas_online = fields.Integer(string='Cantidad de horas online')

    cantidad_horas_presencial = fields.Integer(string='Cantidad de horas presencial')

