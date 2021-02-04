# -*- coding: utf-8 -*-
{
    'name': "Proyecto",

    'summary': """
        Aprendiendo a programar en odoo""",

    'description': """
        No parare hasta lograrlo
    """,

    'author': "Pinha",
    'website': "http://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/proyecto.xml',
        'views/templates.xml',
        'views/informacion.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
