##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route
from odoo.tools import config
from werkzeug.exceptions import Forbidden, NotFound


class femebaPartnerWebsite(WebsiteSale):

    def _get_mandatory_billing_fields(self):
        # para no romper los test de odoo
        res = super(femebaPartnerWebsite, self)._get_mandatory_billing_fields()
        return res + [
            "main_id_category_id", "main_id_number",
            "afip_responsability_type_id", "title", 'cargo_id',
            'especialidad_id', 'university', 'entidad_id'
        ]

    def _checkout_form_save(self, mode, checkout, all_values):
        checkout['mobile'] = checkout['phone']
        checkout['phone'] = False
        res = super(femebaPartnerWebsite, self)._checkout_form_save(
            mode=mode, checkout=checkout, all_values=all_values)
        return res

    def _add_to_newsletter(self, data):
        email = data['email']
        list_id = request.env['mail.mass_mailing.list'].sudo().search([('name', '=', 'Newsletter')])
        Contacts = request.env['mail.mass_mailing.contact'].sudo()
        name, email = Contacts.get_name_email(email)

        contact_ids = Contacts.search([
            ('list_ids', 'in', [int(list_id.id)]),
            ('email', '=', email),
        ], limit=1)
        if not contact_ids:
            # inline add_to_list as we've already called half of it
            Contacts.create({'name': data['name'],
                             'email': email,
                             'title_id': data['title'],
                             'country_id': data['country_id'] and int(data['country_id']),
                             'list_ids': [(6, 0, [list_id.id])]})
        return True

    def checkout_form_validate(self, mode, all_form_values, data):
        if data['newsletter'] == 'si':
            self._add_to_newsletter(data)

        if int(data['partner_id']) > 0:
            data['commercial_partner_id'] = data['partner_id']
        error, error_message = super(
            femebaPartnerWebsite, self).checkout_form_validate(
                mode=mode, all_form_values=all_form_values, data=data)
        write_error, write_message = \
            request.env['res.partner'].sudo().try_write_commercial(
                all_form_values)
        if write_error:
            error.update(write_error)
            error_message.extend(write_message)
        write_error, write_message = \
            request.env['res.partner'].sudo().try_femeba_fields(
                all_form_values)
        if write_error:
            error.update(write_error)
            error_message.extend(write_message)
        return error, error_message

    @route()
    def address(self, **kw):
        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
        order = request.website.sale_get_order()

        response = super(femebaPartnerWebsite, self).address(**kw)
        document_categories = request.env[
            'res.partner.id_category'].sudo().search([])
        afip_responsabilities = request.env[
            'afip.responsability.type'].sudo().search([])
        titles = request.env[
            'res.partner.title'].sudo().search([])
        cargos = request.env[
            'res.partner.cargo'].sudo().search([])
        especialidades = request.env[
            'res.partner.especialidad'].sudo().search([])
        entidades = request.env[
            'res.partner.entidad'].sudo().search([])
        convenios = request.env[
            'res.partner.convenio'].sudo().search([])
        uid = request.session.uid or request.env.ref('base.public_user').id
        Partner = request.env['res.users'].browse(uid).partner_id
        Partner = Partner.with_context(show_address=1).sudo()
        response.qcontext.update({
            'document_categories': document_categories,
            'afip_responsabilities': afip_responsabilities,
            'titles': titles,
            'cargos': cargos,
            'especialidades': especialidades,
            'entidades': entidades,
            'convenios': convenios,
            'partner': Partner,
        })

        return response

    # TODO review: Aca podria ser necesario pasar el afip_responsabilities
    @route()
    def checkout(self, **post):
        super(femebaPartnerWebsite, self).checkout(**post)
        # _response = super(femebaPartnerWebsite, self).checkout(**post)
        order = request.website.sale_get_order()
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            return request.redirect('/shop/address')

        # --------------------------------------------------------------------
        # Odoo original code
        # for f in self._get_mandatory_billing_fields():
        #     if not order.partner_id[f]:
        #         return request.redirect('/shop/address?partner_id=%d' %
        #             order.partner_id.id)
        # Our code
        mandatory_billing_fields = self._get_mandatory_billing_fields()
        commercial_billing_fields = ["main_id_category_id", "main_id_number",
                                     "afip_responsability_type_id", 'title', 'cargo_id',
                                     'especialidad_id', 'university', 'entidad_id']
        for item in commercial_billing_fields:
            mandatory_billing_fields.pop(mandatory_billing_fields.index(item))

        for f in mandatory_billing_fields:
            if not order.partner_id[f]:
                return request.redirect(
                    '/shop/address?partner_id=%d' % order.partner_id.id)
        for f in commercial_billing_fields:
            if not order.partner_id.commercial_partner_id[f]:
                return request.redirect(
                    '/shop/address?partner_id=%d' % order.partner_id.id)
        # end
        # --------------------------------------------------------------------

        values = self.checkout_values(**post)

        values.update({'website_sale_order': order})

        # Avoid useless rendering if called in ajax
        if post.get('xhr'):
            return 'ok'
        return request.render("website_sale.checkout", values)
