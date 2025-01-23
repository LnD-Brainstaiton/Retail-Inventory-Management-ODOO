from odoo import models, fields

class RetailProductStock(models.Model):
    _name = 'retail.product.stock'
    _description = 'Retail Product Stock'

    product_id = fields.Many2one('product.product', string="Product", required=True)  # Many2one to Product
