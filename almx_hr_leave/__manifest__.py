# -*- coding: utf-8 -*-
{
    'name': "almx_hr_leave",

    'summary': """
        Bloquea la edición de la descripción en ausencias confirmadas""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Celia Hernandez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hr_leave_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
