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
    'name': "almx_pricelock",

    'summary': """
       Bloquea el precio de venta""",

    'description': """
        Este modulo crea un grupo llamado "Editar precio de venta" en el cuál, solo los que estén adentro del grupo podrán
        editar este precio.
    """,

    'author': "Celia Hernandez",
    'website': "www.alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '16',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
