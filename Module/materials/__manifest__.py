# -*- coding: utf-8 -*-
{
    'name': "Materials",
    'summary': "Module for Material Management",
    'description': "",
    'author': "Hersyanda Putra Adi",
    'website': "https://www.hpaa.space",
    'category': 'Inventory',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        # security access
        'security/ir.model.access.csv',

        # views
        'views/supplier.xml',
        'views/materials.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
