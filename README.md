# Retail Inventory Management

## Description
**Retail Inventory Management** is a tailored Odoo module designed to streamline inventory, stock, procurement, and sales operations for retail businesses. This module offers comprehensive features, including stock adjustments, stock movement tracking, custom alerts, warehouse management, and insightful analytics, to enhance efficiency and decision-making.

---

## Features
- **Inventory Stock Adjustment**: Adjust stock levels with custom reasons and validations.
- **Stock Move History**: Track stock movement across locations with detailed records.
- **Stock Alerts**: Stay informed with alerts for low stock or critical thresholds.
- **Warehouse Management**: Manage stock across multiple locations efficiently.
- **Analytics and Reports**: Generate insightful reports for inventory performance.

---

## Installation

### Prerequisites
- **Odoo Version**: 18
- **Python Version**: 3.7 or higher
- Ensure Odoo is properly set up on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Copy the module folder into your Odoo **addons** directory.
3. Restart the Odoo server:
   ```bash
   ./odoo-bin -c odoo.conf -u all
   ```
4. Navigate to the **Apps** menu in the Odoo backend.
5. Search for "Retail Inventory Management" and install the module.

---

## Usage

### Key Workflows:
1. **Stock Adjustments**:
   - Navigate to the **Stock Adjustments** menu.
   - Select a product, input adjustments, and provide a reason.
   - Confirm the adjustment to update stock levels.
2. **Stock Movement**:
   - Go to **Stock Movements** and create a new record.
   - Specify the source and destination locations, product, and quantity.
   - Confirm to update the stock across locations.
3. **Reports and Alerts**:
   - Access analytics dashboards for insights into stock levels and trends.
   - Enable alerts to monitor critical stock levels.

---

## Models

### Stock Inventory
Manages stock levels for products at specific locations.

| Field                 | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `product_id`          | Many2one  | Product being tracked.          |
| `quantity`            | Float     | Quantity available in stock.    |
| `stock_location`      | Many2one  | Location of the product.        |
| `stock_value`         | Float     | Computed stock value.           |

### Inventory Adjustment
Handles stock level adjustments with detailed tracking.

| Field                 | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `product_id`          | Many2one  | Product being adjusted.         |
| `current_quantity`    | Float     | Current quantity in stock.      |
| `adjusted_quantity`   | Float     | Adjusted quantity.              |
| `adjustment_reason`   | Text      | Reason for adjustment.          |
| `state`               | Selection | Adjustment status (Draft/Confirmed). |

### Stock Movement
Tracks movements of stock between locations.

| Field                 | Type      | Description                     |
|-----------------------|-----------|---------------------------------|
| `product_id`          | Many2one  | Product being moved.            |
| `quantity`            | Float     | Quantity being moved.           |
| `source_location_id`  | Many2one  | Source location of the product. |
| `destination_location_id` | Many2one | Destination location.        |
| `movement_type`       | Selection | Receipt, Delivery, or Transfer. |
| `state`               | Selection | Movement status (Draft/Confirmed). |

---

## Views

### Stock Operation Views
- **Tree View**: Lists all stock operations with summarized details.
- **Form View**: Detailed interface for creating and managing operations.

---

## Security
Define user roles and access rights to ensure secure operations.

#### `ir.model.access.csv`
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_stock_inventory_user,access_stock_inventory_user,model_stock_inventory,base.group_user,1,0,0,0
access_stock_inventory_manager,access_stock_inventory_manager,model_stock_inventory,base.group_system,1,1,1,1
```

---

## Testing

### Test Scenarios:
1. **Stock Adjustment Validation**:
   - Attempt to adjust stock with zero or negative quantities.
   - Verify the system raises a validation error.
2. **Stock Movement Confirmation**:
   - Create a draft stock movement.
   - Confirm the movement and ensure stock levels update correctly.
3. **Alerts**:
   - Set critical stock thresholds.
   - Verify alerts trigger when stock drops below the threshold.

---

## Future Enhancements
- Dashboard widgets for quick insights.
- Integration with point-of-sale (POS) systems.
- Bulk stock adjustments and imports.
- Barcode scanning support for stock operations.

---


## Contributors
- **[Md. Sadat Kabir Shafin]** - Module Development

---

## Contact
For questions, suggestions, or contributions, feel free to reach out to [sadatkabirshafin@gmail.com].

---
