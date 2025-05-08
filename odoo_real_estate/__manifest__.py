{
    'name': "Odoo Real Estate",
    'version': '1.0.0',
    'summary': "Real estate management app for brokers",
    'description': "Real estate management app, to help manage sales, properties, statuses, etc.",
    'author': 'Abraham Mahanaim',
    'depends': ['base'],
    'category': 'Applications',
    'data': [
        # Data
        'data/dro.rs.property.transaction.state.csv',

        # Security
        'security/ir.model.access.csv',

        # Views
        'views/real_estate_property_type_view.xml',
        'views/real_estate_property_spec_view.xml',
        'views/real_estate_property_availability.xml',
        'views/real_estate_property_client_view.xml',
        'views/real_estate_property_transaction_view.xml',
        'views/real_estate_property_transaction_state_view.xml',
        'views/menu.xml',
    ],
    'assets': {
    },
    'images': [
        'static/description/screenshot_app.png',
    ],
    'license': "AGPL-3",
    'application': True,
}
