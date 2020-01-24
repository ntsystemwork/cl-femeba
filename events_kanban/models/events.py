from odoo import api, fields, models


from odoo import api, fields, models, SUPERUSER_ID


class Event(models.Model):
    _name = "event.event"
    _inherit = "event.event"

    def _get_default_stage_id(self):
        """ Gives default stage_id """
        return self.env['event.stage'].search([('sequence', '=', '0')])

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('id', 'in', stages.ids)]
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

    # group = fields.One2many("event.event", "stage_id", "Etapa")
    stage_id = fields.Many2one(
        "event.stage",
        string="Stage",
        default=_get_default_stage_id,
        group_expand='_read_group_stage_ids',
    )

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    def _get_default_stage_id(self):
        """ Gives default stage_id """
        return self.env['event.stage'].search([('sequence', '=', '0')])

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('id', 'in', stages.ids)]
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

    # group = fields.One2many("event.event", "stage_id", "Etapa")
    stage_id = fields.Many2one(
        "event.stage",
        string="Stage",
        default=_get_default_stage_id,
        group_expand='_read_group_stage_ids',
    )
    color = fields.Integer('Kanban Color Index')
