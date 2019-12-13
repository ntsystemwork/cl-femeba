from odoo import api, fields, models

class Link(models.Model):
    _inherit = "event.event"

    survey_link = fields.Char(string="Link de la encuesta", size=100)