# -*- coding: utf-8 -*-
{
    'name': "DaskTech - Código de barras.",

    'summary': """
        Oculta el botón de validar en el modulo de código de barras""",

    'description': """
        Permite tener una mejor gestión de los movimientos de inventario, ocultando el botón de validar para el módulo de código de barras (barcode).
    """,

    'author': "Celia Hernandez",
    'website': "www.dasktech.mx",

    'category': 'Inventory',
    'version': '16',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','stock_barcode'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/groups.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'almx_barcode/static/src/xml/stock_barcode_inherit.xml',
        ],
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
