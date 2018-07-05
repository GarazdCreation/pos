# -*- coding: utf-8 -*-
{
    'name': 'Garazd restriction of POS User',
    'version': '10.0.1.0.1',
    'category': 'Point of Sales',
    'author': 'Garazd Creation',
    'website': "https://garazd.biz",
    'summary': """
        Limit the POS User to available Points of Sale.
    """,
    'description': 'Allow setting available Points of Sales for users. Restrict access for POS users to Points of Sales.',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'security/pos_user_restrict_security.xml',
        'views/res_users_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
