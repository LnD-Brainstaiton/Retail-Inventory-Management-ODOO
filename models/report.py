from odoo import models, fields, api

class RetailInventoryReport(models.Model):
    _name = 'retail.inventory.report'
    _description = 'Retail Inventory Report'
    _auto = False  # This model is based on SQL views, not a standard database table.

    product_id = fields.Many2one('product.product', string='Product')
    category_id = fields.Many2one('product.category', string='Category')
    available_qty = fields.Float(string='Available Quantity')
    sold_qty = fields.Float(string='Sold Quantity')
    revenue = fields.Float(string='Revenue')
    low_stock_alert = fields.Boolean(
        string='Low Stock', compute='_compute_low_stock_alert', store=True
    )

    @api.depends('available_qty')
    def _compute_low_stock_alert(self):
        for record in self:
            record.low_stock_alert = record.available_qty < 10  # Adjust threshold as needed

    @api.model
    def init(self):
        """Define the SQL view for the report."""
        # Drop the view if it already exists
        self.env.cr.execute("""
            DROP VIEW IF EXISTS retail_inventory_report;
        """)

        # Recreate the view
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW retail_inventory_report AS (
                SELECT
                    p.id AS id,
                    p.id AS product_id,
                    pt.categ_id AS category_id,
                    COALESCE(SUM(CASE 
                        WHEN sl.usage = 'internal' THEN sq.quantity - sq.reserved_quantity 
                        ELSE 0 
                    END), 0) AS available_qty,
                    COALESCE(SUM(sol.product_uom_qty), 0) AS sold_qty,
                    COALESCE(SUM(sol.price_total), 0) AS revenue,
                    CASE 
                        WHEN COALESCE(SUM(CASE 
                            WHEN sl.usage = 'internal' THEN sq.quantity - sq.reserved_quantity 
                            ELSE 0 
                        END), 0) < 10 THEN TRUE
                        ELSE FALSE
                    END AS low_stock_alert
                FROM product_product p
                LEFT JOIN product_template pt ON p.product_tmpl_id = pt.id
                LEFT JOIN stock_quant sq ON sq.product_id = p.id
                LEFT JOIN stock_location sl ON sq.location_id = sl.id
                LEFT JOIN sale_order_line sol ON sol.product_id = p.id
                WHERE sl.usage = 'internal'
                GROUP BY p.id, pt.categ_id
            );
        """)

