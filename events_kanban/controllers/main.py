# -*- coding: utf-8 -*-

import babel.dates
import re
import werkzeug
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request


class WebsiteEventController(http.Controller):  
  
    def _process_registration_details(self, details):
        ''' Process data posted from the attendee details form. '''
        registrations = {}
        global_values = {}
        for key, value in details.items():
            counter, field_name = key.split('-', 1)
            if counter == '0':
                global_values[field_name] = value
            else:
                registrations.setdefault(counter, dict())[field_name] = value
        for key, value in global_values.items():
            for registration in registrations.values():
                registration[key] = value
        return list(registrations.values())

  
    @http.route(['/event/<model("event.event"):event>/registration/confirm'], type='http', auth="public", methods=['POST'], website=True)
    def registration_confirm(self, event, **post):
        Attendees = request.env['event.registration']
        registrations = self._process_registration_details(post)

        for registration in registrations:
            registration['event_id'] = event
            Attendees += Attendees.sudo().create(
                Attendees._prepare_attendee_values(registration))

        return request.render("website_event.registration_complete", {
            'attendees': Attendees.sudo(),
            'event': event,
        })
