# -*- coding: utf-8 -*-
{
    'name': "on_click",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/cliente.xml',
        'views/organizador.xml',
        'views/place.xml',
        'views/producto.xml',
        'views/evento.xml',
        'views/evento_extended.xml',
        'views/contrato.xml',
        'views/menu.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'on_click/static/src/scss/style.scss',
        ],
    },
}

