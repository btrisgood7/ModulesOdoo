# -*- coding: utf-8 -*-
{
    'name': "Alamex Recompensas",

    'summary': """
        Sistema básico de puntos de lealtad por compras.""",

    'description': """
        En este módulon agregamos un pequeño sistema básico de recompensas, con puntos acumulables para el uso
        de nuestros clientes más leales. :)
    """,

    'author': "Alamex",
    'website': "www.alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/respartner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
