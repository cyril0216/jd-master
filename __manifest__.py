#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Cyril

{
    'name': "京东茅台助手",
    'summary': 'design by Cyril',
    'version': '1.0',
    'category': "基础",
    'sequence': 10,
    'author': 'Cyril',
    'website': 'https://github.com/cyril0216/jd-master',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/jd_cookie.xml',
        'views/menu_main.xml',
        'views/jd_access_token.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [
        # 'static/src/xml/test.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """

""",
}
