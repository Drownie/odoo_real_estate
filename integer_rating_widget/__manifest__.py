{
    'name'          : "Integer Rating Widget",
    'version'       : "1.0",
    'depends'       : ['web'], 
    'category'      : 'Widget',
    'author'        : "Abraham Mahanaim",
    'description'   : "Rating Widget to Support Integer fields",
    'assets': {
        'web.assets_backend': [
            "integer_rating_widget/static/src/js/integer_rating.js",
            "integer_rating_widget/static/src/xml/integer_rating.xml",
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'application': False,
    'license': "AGPL-3",
}