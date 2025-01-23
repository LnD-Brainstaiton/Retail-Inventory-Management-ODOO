from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    categ_id = fields.Many2one('product.category', string="Category")  # Many2one to Product Category
    retail_notes = fields.Text(string="Retail Notes")
    brand = fields.Char(string="Brand")

class ProductProduct(models.Model):
    _inherit = 'product.product'

    stock_level = fields.Float(string="Stock Level", compute="_compute_stock_level")
    inventory_report_ids = fields.One2many('retail.inventory.report', 'product_id', string='Inventory Report')

    def _compute_stock_level(self):
        for product in self:
            product.stock_level = sum(product.stock_quant_ids.mapped('quantity'))
