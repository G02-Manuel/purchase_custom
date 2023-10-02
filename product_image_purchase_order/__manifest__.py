{
    'name': "Product Image On Purchase Order Line",
    'version': "12.0.0.1",
    'category': "Purchase",
    'summary': "Display product image on purchase order report.",
    'description': "Display product image on purchase order report.",
    'author': "Gerlin Matos",
    'depends': ['base', 'purchase'],
    'data': [
        'report/purchase_order_report.xml',
        'report/purchase_reports.xml',
        'views/view_purchase_order.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
