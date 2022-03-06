# -*- coding: utf-8 -*-
{
    'name': "Alsaree3 Vender Ref",

    # TODO: Change Summary to something relavant to the module
    'summary': """
        Vaping store managment """,

    # TODO: this is a simple module. so 'description' key is not needed. go ahead and delete it
    'description': """
        Vaping store managment
    """,

    # TODO: the author should 'Integrated Path' and website 'https://www.int-path.com'
    'author': "Aya",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # TODO: category value should relevent to the module (ex: Purchase). 👆🏼 use the above URL for reference
    'category': 'Apps',

    #  TODO: version value should '<odoo verion>.<module version>' so for this module it should be '15.1'
    'version': '0.1',

    # TODO: application tags are only for large scale modules. so delete this key
    'application': True,


    # any module necessary for this one to work correctly
    # TODO: the comment above explains the usage of 'depends' key. for this module our only dependcies is 'purchase' module
    #   feel free to ask when you need to know the needed dependcies modules in the future
    'depends': ['base', "account","sale"],

    # TODO: sense we are not importing from sucurity or view folder. we should go ahead & delete these folder from this repo
    #   And also empety the list below from the comments
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        
    ],
    # TODO: we didn't use demo data for this module. So go ahead and delete both the folder and the key blow
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
