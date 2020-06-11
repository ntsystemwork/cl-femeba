from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'


    @api.model
    def try_femeba_fields(self, data):
        """ User for website. capture the validation errors and return them.
        return (error, error_message) = (dict[fields], list(str()))
        """
        error = dict()
        error_message = []
        title = data.get('title', False)
        professional_registration = data.get('professional_registration', False)
        cargo_id = data.get('cargo_id', False)
        especialidad_id = data.get('especialidad_id', False)
        university = data.get('university', False)
        organization = data.get('organization', False)
        entidad = data.get('entidad', False)
        convenio_id = data.get('convenio_id', False)
        comment = data.get('comment', False)

        if title and cargo_id and especialidad_id and university and entidad:
            commercial_partner = self.env['res.partner'].sudo().browse(
                int(data.get('commercial_partner_id', False)))
            try:
                values = {
                    'title': int(title),
                    'cargo_id': int(cargo_id),
                    'especialidad_id': int(especialidad_id),
                    'university': university,
                    'entidad_id': int(entidad),
                    'professional_registration':
                        professional_registration
                        if professional_registration else False,
                    'organization':
                        organization
                        if organization else False,
                    'convenio_id':
                        int(convenio_id)
                        if convenio_id else False,
                    'comment':
                        comment
                        if comment else False,
                }
                commercial_fields = ['title']
                values = commercial_partner.remove_readonly_required_fields(
                    commercial_fields, values)
                with self.env.cr.savepoint():
                    commercial_partner.write(values)
            except Exception as exception_error:
                _logger.error(exception_error)
                error['title'] = 'error'
                error_message.append(_(exception_error))
        return error, error_message

