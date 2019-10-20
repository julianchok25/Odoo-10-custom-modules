# -*- coding: utf-8 -*-
{
    'name': "test_quadi",

    'summary': """
        Test for quadi company with different requirements
        """,

    'description': """
        Solution to manage votes with ERP odoo
    """,

    'author': "Julian Villegas",
    'website': "https://medium.com/@david.villegasplus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Quadi',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/idea.xml',
        'views/vote.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable":True,
    "application":True
}