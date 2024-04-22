# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'HCQ Inventory',
    'version': '1.0.0',
    'category': 'Inventory',
    'sequence': -100,
    'summary': 'Inventory System for HCQ Marketing',
    'description': """""",
    'depends': [ ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/item.xml',  
        ],
    'demo': [],
    'installable': True,
    'assets': {}
       
}