# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Lead Work Days',
    'version': '1.0',
    'summary': 'Adds work_days field to crm.lead model',
    'description': "This module adds a calculated field “Work Days” to the CRM Lead,which shows the number of days between the date of lead creation and the current date.",
    'website': 'https://www.odoo.com/app/crm',
    'category': 'Sales/CRM',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_work_days_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
