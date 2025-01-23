from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_field = fields.Char(string="Custom Field")
    sale_order_count = fields.Integer(string="Sale Order Count", compute='_compute_sale_order_count', store=True)

    @api.depends('order_line')
    def _compute_sale_order_count(self):
        for order in self:
            # Count sale orders related to this purchase order via the order lines
            order.sale_order_count = len(order.order_line.mapped('sale_order_id'))


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    custom_discount = fields.Float(string="Discount (%)")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")  # Added sale_order_id field

    def compute_discounted_price(self):
        for line in self:
            # custom discount to the price unit
            line.price_unit = line.price_unit * (1 - line.custom_discount / 100)
