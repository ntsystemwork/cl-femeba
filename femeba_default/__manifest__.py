# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019 NT System Work (http://www.ntsystemwork.com)
#    All Rights Reserved.
#
# -----------------------------------------------------------------------------
{
    'name': 'femeba',
    'version': '11.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para femeba',
    'author': 'NT System Work',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        # si es enterprise poner standard_depends_ee si es community standard_depends_ce
        'standard_depends_xx',

        # utilitarios adicionales
        'backend_theme',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # --------------------------------------------

    # if Enterprise it installs in a different directory than community
    'Enterprise': False,

    # port where odoo starts serving pages
    'port': '8069',

    'repos': [
        {'usr': 'ntsystemwork', 'repo': 'cl-femeba', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'rafi16jan-backend-theme',
         'branch': '11.0'},

        {'usr': 'jobiols', 'repo': 'adhoc-odoo-argentina', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-sale', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
         'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-sale', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-odoo-support', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-partner-contact', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-web', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-tools', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-social', 'branch': '11.0'},
        {'usr': 'jobiols', 'repo': 'oca-server-brand', 'branch': '11.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '11.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],
}

