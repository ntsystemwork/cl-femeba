from odoo import api, fields, models


class Event(models.Model):
    _name = "event.event"
    _inherit = "event.event"

    # group = fields.One2many("event.event", "stage_id", "Etapa")
    stage_id = fields.Many2one(
        "event.stage",
        string="Stage"
    )
