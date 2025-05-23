{
    'name'          : "Integer Rating Widget",
    'version'       : "1.0",
    'depends'       : ['base'], 
    'category'      : 'Widget',
    'author'        : "Abraham Mahanaim",
    'description'   : "Rating Widget to Support Integer fields",
    'assets': {
        'web.assets_backend': [
            'rating_widget/static/src/style/rating.scss',
            'rating_widget/static/src/xml/rating.xml',
            'rating_widget/static/src/js/rating.js',
        ],
    },
    'application': False,
    "lisence":"AGPL-3"
}