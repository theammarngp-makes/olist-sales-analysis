# SQL Query Execution Index & Logic Mapping

## Overview
This index provides a comprehensive breakdown of the production SQL scripts within this repository. It serves as a technical blueprint for engineers, data analysts, and stakeholders to understand the underlying logic, tables, and optimization strategies employed to generate the project's core business intelligence metrics.

---

## 1. Core Revenue & Performance KPIs
* **File Reference:** `01_sales_kpis.sql`
* **Business Objective:** Establishes foundational business health indicators (Gross Revenue, Customer Footprint, and Average Order Value) for high-level executive tracking.

### Query Architecture & Logic
* **Optimization Strategy:** Implements a Common Table Expression (CTE) named `kpis` to pre-aggregate line-level financials per unique order and customer entity before executing final global aggregations. This prevents inflation of unique counts and ensures mathematical accuracy.
* **Calculation Logic:**
  * **Gross Value per Line:** `SUM(oi.freight_value + oi.price)`
  * **Total Revenue:** Global sum of the pre-aggregated order totals.
  * **Total Customers:** Unique deduplicated count of `customer_unique_id`.
  * **Average Order Value (AOV):** Mean value of the total gross amounts across all unique orders.

### Schema Relationships

[customers] ──(customer_id)──> [orders] ──(order_id)──> [order_items]

---

## 2. Temporal Revenue Trend Analysis
* **File Reference:** `02_monthly_revenue.sql`
* **Business Objective:** Measures revenue velocity and exposes macro-level seasonal patterns across the fiscal timeline.

### Query Architecture & Logic
* **Extraction Strategy:** Utilizes a date manipulation function to isolate the month from the central transaction ledger.
* **Calculation Logic:** Groups and aggregates the combined price and freight values by the extracted month name (`DATE_FORMAT(o.order_purchase_timestamp, "%M")`).
* **Sorting Matrix:** Ordered chronologically by month to map continuous business performance trends.

### Schema Relationships
[orders] ──(order_id)──> [order_items]

---

## 3. Product Portfolio & Category Performance
* **File Reference:** `03_category_revenue.sql`
* **Business Objective:** Ranks product categories by gross economic output to isolate high-value revenue drivers and identify long-tail operational distribution.

### Query Architecture & Logic
* **Aggregation Strategy:** Joins the dimensional product table with the transactional item table to sum gross value across unique product categories.
* **Calculation Logic:** `SUM(oi.price + oi.freight_value)` aggregated under `p.product_category_name`.
* **Sorting Matrix:** Ranked in descending order (`DESC`) to instantly bubble up top-performing product categories for inventory and marketing prioritization.

### Schema Relationships
[products] ──(product_id)──> [order_items]

---

## 4. Geographic & Regional Revenue Distribution
* **File Reference:** `04_state_city_revenue.sql`
* **Business Objective:** Aggregates financial performance by geographic boundaries to expose regional market concentration risks and target areas for expansion.

### Query Architecture & Logic
* **Integration Strategy:** Connects transactional records down to the customer's physical registration location.
* **Calculation Logic:** Aggregates line-item financial values by regional dimensions (State and City levels).
* **Sorting Matrix:** Grouped and ordered by total regional revenue contribution to identify core regional strongholds.

### Schema Relationships
[customers] ──(customer_id)──> [orders] ──(order_id)──> [order_items]