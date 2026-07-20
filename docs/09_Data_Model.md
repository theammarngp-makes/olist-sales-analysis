# Data Model

Based on the standard Olist Brazilian E-Commerce Public Dataset (Kaggle) schema. Verify column names against your local CSVs before publishing externally — Kaggle has released minor schema revisions over time.

## Core Tables

### `orders`
| Column | Type | Description |
|---|---|---|
| order_id | string (PK) | Unique order identifier |
| customer_id | string (FK) | Links to `customers` |
| order_status | string | delivered, shipped, canceled, etc. |
| order_purchase_timestamp | datetime | When the order was placed |
| order_delivered_customer_date | datetime | Actual delivery date |
| order_estimated_delivery_date | datetime | Delivery date promised at purchase |

### `order_items`
| Column | Type | Description |
|---|---|---|
| order_id | string (FK) | Links to `orders` |
| order_item_id | int | Sequence number within an order |
| product_id | string (FK) | Links to `products` |
| seller_id | string (FK) | Links to `sellers` |
| price | decimal | Item price (excludes freight) |
| freight_value | decimal | Shipping cost for the item |

### `customers`
| Column | Type | Description |
|---|---|---|
| customer_id | string (PK) | Order-level customer key (see caveat below) |
| customer_unique_id | string | Persistent customer identity across orders |
| customer_state | string | Brazilian state abbreviation |
| customer_city | string | City name |

> **Important caveat:** `customer_id` is generated per order in this public dataset; `customer_unique_id` is the correct key for any repeat-purchase or retention analysis. Using `customer_id` for retention metrics will overstate the one-time-buyer rate. Confirm which key the current SQL uses — see `data_quality_assessment.md`.

### `products`
| Column | Type | Description |
|---|---|---|
| product_id | string (PK) | Unique product identifier |
| product_category_name | string | Category (Portuguese; translate via `product_category_name_translation`) |

### `payments`
| Column | Type | Description |
|---|---|---|
| order_id | string (FK) | Links to `orders` |
| payment_type | string | credit_card, boleto, voucher, debit_card |
| payment_installments | int | Number of installments |
| payment_value | decimal | Total paid |

### `sellers`
| Column | Type | Description |
|---|---|---|
| seller_id | string (PK) | Unique seller identifier |
| seller_state | string | Seller's state |

### `order_reviews`
| Column | Type | Description |
|---|---|---|
| review_id | string (PK) | Unique review identifier |
| order_id | string (FK) | Links to `orders` |
| review_score | int (1–5) | Customer satisfaction score |

## Relationships

```
customers (1) ──< (many) orders (1) ──< (many) order_items >── (1) products
                                    │
                                    └──< (many) payments
                                    └──< (0..1) order_reviews
order_items >── (many) ── (1) sellers
```

## Granularity

The natural grain of the joined dataset is **one row per order item** (an order with 3 products yields 3 rows). Any revenue KPI must sum, not count rows, to avoid overstating order counts — confirm this is handled correctly in `sql/sales_kpis.sql`.

## Limitations

- Dataset is anonymized and covers a fixed historical window (2016–2018) — not live data.
- Geolocation data is provided separately by zip-code prefix and is approximate, not exact address-level.
- `customer_id` vs `customer_unique_id` distinction (above) is the single most important gotcha in this schema for any retention-related claim.

## ER Diagram Specification

For anyone producing the actual diagram image (e.g., in dbdiagram.io, Lucidchart, or draw.io), here is the exact specification:

**Entities and key fields:**
- `customers` (PK: customer_id; also holds customer_unique_id, customer_state, customer_city)
- `orders` (PK: order_id; FK: customer_id → customers)
- `order_items` (composite PK: order_id + order_item_id; FK: order_id → orders; FK: product_id → products; FK: seller_id → sellers)
- `products` (PK: product_id; holds product_category_name)
- `sellers` (PK: seller_id; holds seller_state)
- `payments` (FK: order_id → orders; holds payment_type, payment_value)
- `order_reviews` (PK: review_id; FK: order_id → orders; holds review_score)

**Cardinalities:**
- customers 1 ──< orders (one customer, many orders — using customer_unique_id)
- orders 1 ──< order_items (one order, many line items)
- products 1 ──< order_items (one product, many line items across orders)
- sellers 1 ──< order_items (one seller, many line items)
- orders 1 ──< payments (an order can have multiple payment records, e.g. split payments)
- orders 1 ──0/1 order_reviews (an order has zero or one review)

**Layout suggestion:** place `orders` centrally with `customers` to its left and `order_items` to its right; hang `products` and `sellers` off `order_items`; hang `payments` and `order_reviews` below `orders`. This mirrors the transactional flow (customer → order → fulfillment → payment/review) and reads left-to-right the way a stakeholder would narrate it.
