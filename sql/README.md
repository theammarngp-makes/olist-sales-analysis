# Production SQL Analytics Engine

## Overview
This directory contains the production-grade SQL scripts used to extract, aggregate, and analyze high-priority business metrics from the Olist e-commerce database. These scripts act as the data transformation layer that feeds the reporting metrics into the corporate visualization platforms.

All queries are structured to maintain performance efficiency, utilizing Common Table Expressions (CTEs), optimal inner/left joins, and standardized aggregation functions.

## Query Portfolio & Matrix

The analytical engine is structured into four primary reporting blocks, each addressing specific strategic business operations:

| File Name | Target Business KPI / Metric | Primary Tables Utilized | Strategic Analytical Value |
|:---|:---|:---|:---|
| `01_sales_kpis.sql` | Gross Revenue, Unique Customer Footprint, Average Order Value (AOV) | `orders`, `order_items`, `customers` | Establishes the core health metrics of the enterprise for high-level executive review. |
| `02_monthly_revenue.sql` | Temporal Revenue Trends (Month-over-Month) | `orders`, `order_items` | Evaluates seasonality, operational growth, and macro-level sales velocity patterns. |
| `03_category_revenue.sql` | Product Category Performance Rankings | `products`, `order_items` | Identifies high-margin categories and reveals product portfolio distribution (Pareto/Long-Tail effects). |
| `04_state_city_revenue.sql` | Geographic Sales Distribution & Density | `orders`, `order_items`, `customers` | Maps market penetration across states/cities to flag concentration risks and expansion opportunities. |

## Database Schema Context
The queries assume a relational star/snowflake schema where:
* `orders` acts as the central transaction ledger linking to `customers` via `customer_id`.
* `order_items` captures line-level transaction data (linking `price` and `freight_value`) connected via `order_id`.
* `products` stores item dimensions linked via `product_id`.

## Operational Syntax Notes
* **Revenue Logic:** Total revenue calculations uniformly reflect the gross economic footprint per transaction line item, computed as:
  $$\text{Total Gross Value} = \text{Item Price} + \text{Freight Value}$$
* **Engine Compatibility:** The syntax utilizes standard ANSI SQL conventions alongside common dialects (e.g., MySQL date functions like `DATE_FORMAT`). If migrating to an alternative data warehouse environment (e.g., Snowflake or BigQuery), swap local date functions to their respective warehouse dialects (e.g., `DATE_TRUNC` or `FORMAT_TIMESTAMP`).

---
*For the automated ingestion logic and pre-database data exploration, reference the `/python` directory. For the final visualization layer built from these outputs, reference the `/dashboard` directory.*