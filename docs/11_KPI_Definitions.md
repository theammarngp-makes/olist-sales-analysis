# KPI Definitions

| KPI | Formula | Business Importance | Decision Supported | Primary Stakeholder |
|---|---|---|---|---|
| Total Revenue | Σ(order item price + freight value) | Top-line health indicator | Growth forecasting | CEO, Finance |
| Total Orders | COUNT(DISTINCT order_id) | Demand/volume signal | Staffing and capacity planning | Operations |
| Average Order Value (AOV) | Total Revenue ÷ Total Orders | Pricing and basket-size health | Pricing and promotion decisions | Sales, Marketing |
| Category Revenue Share | Category Revenue ÷ Total Revenue | Concentration risk indicator | Category prioritization, inventory allocation | Sales, Supply Chain |
| State Revenue Share | State Revenue ÷ Total Revenue | Geographic concentration risk | Regional expansion / marketing spend | Marketing, Finance |
| Monthly Revenue Trend | Revenue grouped by order month | Seasonality detection | Inventory and staffing planning | Operations |
| Repeat Purchase Rate | Customers with 2+ orders (by `customer_unique_id`) ÷ Total Customers | Retention health | Retention program sizing and investment | Customer Success, Marketing |

## Reporting Cadence

| KPI | Cadence | Owner |
|---|---|---|
| Total Revenue, Total Orders, AOV | Monthly | Finance / Sales leadership |
| Category & State Revenue Share | Quarterly (or after any major marketing shift) | Marketing |
| Repeat Purchase Rate | Quarterly | Customer Success |

## Known Edge Cases

- **Repeat Purchase Rate** must be computed using `customer_unique_id`, not `customer_id` (see `09_Data_Model.md`) — using the wrong key will significantly overstate the one-time-buyer rate.
- **AOV** should be computed at the order level (revenue ÷ distinct orders), not the line-item level, or it will understate true order value on multi-item orders.
- **Category Revenue Share** can be distorted by a small number of very-high-price outlier items; consider a secondary median-price view if a category's average looks unrepresentative.
