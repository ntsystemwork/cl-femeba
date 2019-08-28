from odoo import api, fields, models


# Campos: nombre, descripción, secuencia. fond, evento_ids many2many_tags


class EventsStages(models.Model):
    _name = "event.stage"

    name = fields.Char(
        size=30,
        string="Nombre de la etapa"
    )
    descripcion = fields.Char(
        size=30,
        string="Descripción"
    )
    sequence = fields.Integer(
        string="Secuencia"
    )
    fold = fields.Boolean(
        string="Hide in Kanban",
        default=False
    )
    evento_ids = fields.Many2many(
        "event.event",
        "stage_tag_rel",
        "stage_id",
        "event_id",
        string="Eventos"
    )
