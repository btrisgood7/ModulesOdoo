# -*- coding: utf-8 -*-
{
    'name': "almx_guiasm",

    'summary': """
        Agrega campos al modulo de proyectos para el proceso de las guias mecanicas""",

    'description': """
        Agrega el campo de "formatos acabados"
    """,

    'author': "Celia Hernandez",
    'website': "alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'project',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/project_task_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
