# -*- coding: utf-8 -*-
{
    'name': "educational_management_system",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'ems/admission_reg.xml',
        'ems/profiles.xml',
        'ems/menu.xml',
        'ems/reminders.xml',
        'ems/config.xml',
        'data/sequence.xml',
        'ems_reports/pdf_card.xml',
        'ems_reports/excel_card.xml',
        'ems_wizard/wiz.xml',






    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
