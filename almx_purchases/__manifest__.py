# -*- coding: utf-8 -*-
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2026 Elevadores Alamex - www.alam.mx
# All Rights Reserved.
#
# Developer(s): Celia Alessandra Hernandez Alvarado
#               (celia.a@alam.mx)
#
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
{
    'name': "Alamex - Compras",

    'summary': """
        Indicador de pedimento""",

    'description': """
        Indicador de pedimento, en donde este solo se podrá agregar a los IN, aunque estos hayan sido creado mediante una orden parcial.
    """,

    'author': "Celia Hernandez",
    'website': "www.alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '16',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/stock_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
