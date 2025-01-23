{
    'name': 'Retail Inventory Management',
    'version': '1.0.0',
    'summary': 'Custom Inventory Management System for Retail Businesses',
    'description': """
        A tailored module for managing inventory, stock, procurement, and sales for retail businesses.
        Includes features like custom inventory stock adjustment, stock move history, stock alerts, warehouse management and analytics.
    """,
    'author': 'Sadat Kabir',
    'website': '',
    'category': 'Inventory',
    'depends': ['stock', 'sale', 'purchase', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_views.xml',
        'views/product_views.xml',
        'views/purchase_views.xml',
        'views/sale_views.xml',
        'views/stock_operation_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
