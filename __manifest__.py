# -*- coding: utf-8 -*-
{
    'name': "HN CONSISA - BO-helpdesk",
    'category': 'Helpdesk',
    'summary': """
        Modulo Exclusivo de Consisa""",
    'author': "Marlon Joel Zelaya Garcia",
    'website': "www.consisa.com",
    'version': '13.0.1.0.1',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'mail',
        'helpdesk',
    ],
    'data': [
        'security/groups.xml',
        #'security/ir.model.access.csv',
        'views/hn_users_inherit.xml',
    ],
    'demo': [
        'demo/base_external_dbsource.xml',
    ],

}