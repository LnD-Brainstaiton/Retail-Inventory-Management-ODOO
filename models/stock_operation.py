from odoo import models, fields

class StockLocation(models.Model):
    _inherit = 'stock.location'
    _description = 'Stock Location for Retail'

    location_type = fields.Selection([
        ('internal', 'Internal'),
        ('transit', 'Transit'),
        ('inventory', 'Inventory'),
    ], string="Location Type", default='internal')

    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse")
    description = fields.Text(string="Description")

    # Create a relation with the Stock Move model
    stock_move_ids = fields.One2many('stock.move', 'source_location_id', string="Stock Moves from This Location")


# Warehouse Model - Extending the Odoo warehouse model
class Warehouse(models.Model):
    _inherit = 'stock.warehouse'
    _description = 'Warehouse for Retail'

    manager = fields.Many2one('res.users', string="Warehouse Manager")
    location_ids = fields.One2many('stock.location', 'warehouse_id', string="Stock Locations")

    # Warehouse has multiple stock moves
    stock_move_ids = fields.One2many('stock.move', 'warehouse_id', string="Stock Moves")


# Stock Move Model - Extending the Odoo stock move model
class StockMove(models.Model):
    _inherit = 'stock.move'
    _description = 'Stock Movement for Retail'

    product_id = fields.Many2one('product.product', string="Product", required=True)
    source_location_id = fields.Many2one('stock.location', string="Source Location", required=True)
    destination_location_id = fields.Many2one('stock.location', string="Destination Location", required=True)
    quantity = fields.Float(string="Quantity")
    move_date = fields.Datetime(string="Move Date", default=fields.Datetime.now)
    move_type = fields.Selection([('in', 'Incoming'), ('out', 'Outgoing')], string="Move Type", required=True)

    # Link stock move to sale or purchase order
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")

    # Warehouse relation
    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse", required=True)

    # Additional stock move details like tracking or reference
    reference = fields.Char(string="Reference")


# Stock Adjustment Model -Custom manual adjustments
class StockAdjustment(models.Model):
    _name = 'stock.adjustment'
    _description = 'Stock Adjustment for Retail'

    adjustment_reason = fields.Text(string="Adjustment Reason")
    location_id = fields.Many2one('stock.location', string="Stock Location", required=True)

    # Relating stock adjustments to stock moves
    #stock_move_ids = fields.One2many('stock.move', 'inventory_id', string="Stock Moves from Adjustment")

    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft')

    adjustment_date = fields.Datetime(string="Adjustment Date", default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)

    product_id = fields.Many2one('product.product', string="Product")
    adjusted_quantity = fields.Float(string="Adjusted Quantity")

    quantity_before_adjustment = fields.Float(string="Quantity Before Adjustment")
    quantity_after_adjustment = fields.Float(string="Quantity After Adjustment")

    def confirm_adjustment(self):
        # Here add logic to confirm the stock adjustment and create stock moves
        self.state = 'done'





