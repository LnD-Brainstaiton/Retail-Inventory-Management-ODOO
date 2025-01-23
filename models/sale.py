from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string="Custom Field")
    purchase_order_count = fields.Integer(string="Purchase Order Count", compute='_compute_purchase_order_count', store=True)

    @api.depends('order_line')
    def _compute_purchase_order_count(self):
        for order in self:
            # 'purchase_order_id' exists in the order_line model
            order.purchase_order_count = len(order.order_line.mapped('purchase_order_id'))

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    custom_discount = fields.Float(string="Discount (%)")  #custom field for discount
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order')  # Link to Purchase Order

    def compute_discounted_price(self):
        for line in self:
            line.price_unit = line.price_unit * (1 - line.custom_discount / 100)
