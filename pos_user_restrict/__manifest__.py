# -*- coding: utf-8 -*-
#############################################################
#
#    Garazd Creation, Ukraine
#    Copyright (C) 2018-Present Garazd Creation (<https://garazd.biz/>).
#    Author: Yurii Razumovskyi (<support@garazd.biz>)
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
#
#############################################################
{
    'name': 'Restriction of POS User',
    'version': '13.0.1.0.1',
    'category': 'Point of Sale',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz/contactus',
    'license': 'LGPL-3',
    'summary': """Restrict POS Users to allowed Points of Sale.""",
    'description': 'The module allows to restrict access to Points of Sale for POS users.',
    'images': ['static/description/banner.png'],
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_user_restrict_security.xml',
        'views/res_users_views.xml',
    ],
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
