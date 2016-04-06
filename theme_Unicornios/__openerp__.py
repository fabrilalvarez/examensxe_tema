{
    'name': 'Unicornios',
    'description': 'Este tema te dibuja unicornios por doquier para tu sistema ERP Odoo.',
    'category': 'Theme/Hidden',
    'sequence': 1000,
    'version': '1.0',
    'author': 'Francisco S.A.',
    'depends': ['website'],
    'data': [
        'views/layout.xml',
        'views/pages.xml', 
        'views/assets.xml',
        'views/snippets.xml',
        'views/vacaciones.xml',
        'views/quiensomos.xml',
    ],
    'category': 'Theme/Creative',
    'depends': ['website', 'website_blog', 'sale']
}
