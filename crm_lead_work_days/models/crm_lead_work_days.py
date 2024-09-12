# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from datetime import datetime

class CRMLead(models.Model):
    _inherit = 'crm.lead'
    _description = "Lead/Opportunity"

    work_days = fields.Integer(
        string='Work Days',
        compute='_compute_work_days',
        store=True
    )

    @api.depends('create_date')
    def _compute_work_days(self):
        for record in self:
            if record.create_date:
                today = fields.Date.context_today(self)
                create_date = fields.Date.from_string(record.create_date)
                delta = today - create_date
                record.work_days = delta.days
            else:
                record.work_days = 0
