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
        'standard_depends_ce',

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

    # port where odoo starts serving pages
    'port': '8069',
    'repos': [
        {'usr': 'ntsystemwork', 'repo': 'cl-femeba', 'branch': '11.0',
         'ssh': True},
        {'usr': 'ntsystemwork', 'repo': 'nt-addons', 'branch': '11.0',
         'ssh': True},
        {'usr': 'ntsystemwork', 'repo': 'medical', 'branch': '11.0',
         'ssh': True},

        {'usr': 'jobiols', 'repo': 'rafi16jan-backend-theme',
         'branch': '11.0'},

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',
         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',
         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-invoicing', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'patches', 'branch': '11.0'},

        {'usr': 'oca', 'repo': 'queue', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-ux', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-brand', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'manufacture', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'manufacture-reporting', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'ddmrp', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'management-system', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-reporting', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '11.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '11.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],
}
