# -*- coding: utf-8 -*-
{
    'name': "Alsaree3 Vender Ref",

    'summary': """
        Vaping store managment """,

    'description': """
        Vaping store managment
    """,

    'author': "Aya",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Apps',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base', "account","sale"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
