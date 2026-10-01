# -*- coding: utf-8 -*-
{
    'name': "almx_csf",

    'summary': """
        Agrega el campo "Constancia de situación fiscal" al modulo de contactos""",

    'description': """
        Permite al área de ventas y finanzas poder tener una mejor gestion sobre el tema de facturacion de los clientes
    """,

    'author': "Celia Hernandez",
    'website': "alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contacts',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/contacts_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
