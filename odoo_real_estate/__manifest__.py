{
    'name': "Real Estate Management App",
    'version': '17.0.0.1.0',
    'summary': "Real estate management app for brokers",
    'description': "Real estate management app, to help manage sales, properties, statuses, etc.",
    'author': 'Abraham Mahanaim',
    'depends': [
        'base', 
        'integer_rating_widget'
    ],
    'category': 'Applications',
    'data': [
        # Data
        'data/dro.rs.property.transaction.state.csv',

        # Security
        'security/ir.model.access.csv',

        # Views
        'views/res_partner_views.xml',
        'views/dro_rs_property_facility_views.xml',
        'views/dro_rs_property_transaction_state_views.xml',
        'views/dro_rs_property_transaction_views.xml',
        'views/dro_rs_property_type_views.xml',
        'views/dro_rs_property_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ], 
    'assets': {
    },
    'images': [
        'static/description/banner.png',
        'static/description/screenshot_app.png',
    ],
    'license': "AGPL-3",
    'application': True,
}
