# Tableau Dashboard Metadata & Field Dictionary

## Overview
This document serves as the data dictionary and visual mapping guide for the production **E-Commerce Sales Dashboard**. It translates user interface (UI) components and visual variables into their exact database column sources, logical definitions, and aggregation methods. 

This matrix ensures perfect alignment between the data engineering layer (`/sql`), the data verification layer (`/python`), and the final business intelligence layer.

---

## 1. Executive Summary KPI Tile Mapping

The top banner components represent global enterprise performance metrics calculated over the entire dataset footprint.

| Visual Tile Title | UI Display Value | Underlying Business Formula / Field | Source Tables | Aggregation Type | Technical Notes |
|:---|:---|:---|:---|:---|:---|
| **Total Revenue** | $15,843,553 | `price` + `freight_value` | `order_items` | `SUM` | Reflects the gross financial footprint (gross product value plus logistics charges passed to consumers). |
| **Total Orders** | 95,420 | `order_id` | `orders` | `COUNT DISTINCT` | Measures transactional throughput by counting unique completed order IDs. |
| **AOV** | 161 | `SUM(price + freight_value)` / `COUNT(DISTINCT order_id)` | `order_items`, `orders` | `AVERAGE` of Order Sums | Represents the Average Order Value. Aggregated first at the individual order level, then averaged globally. |

---

## 2. Visual Component Data Dictionary

This matrix maps the structural fields utilized to build the dimensional encodings (Axes, Color, Tooltips) for each visualization quadrant.

### A. Temporal Revenue Velocity (Line Chart)
* **Visual Encoding:** X-Axis = Time (Month), Y-Axis = Revenue (Continuous Line)
* **Target Analytical Dimension:** Temporal trends and business seasonality.

| UI Field Name | Mapping Axis / Role | Underlying Data Column | Source Table | Data Type | Functional Description |
|:---|:---|:---|:---|:---|:---|
| **Month** | X-Axis (Columns) | `order_purchase_timestamp` | `orders` | Date / Temporal | Disaggregated and formatted as long month name string (e.g., "January", "February") for chronological profiling. |
| **Total** | Y-Axis (Rows) | Derived `total` field | Composite | Continuous Numeric | The baseline performance line height mapping gross financial intake per month. |

### B. Product Portfolio Performance Matrix (Horizontal Bar Chart)
* **Visual Encoding:** Length = Gross Revenue, Color Intensity = Category Rank vs. Benchmark Line.
* **Target Analytical Dimension:** Category revenue concentration.

| UI Field Name | Mapping Axis / Role | Underlying Data Column | Source Table | Data Type | Functional Description |
|:---|:---|:---|:---|:---|:---|
| **Product Category Name** | Y-Axis (Rows) | `product_category_name` | `products` | Text / String | Primary dimensional split identifying the product domain (e.g., *beleza_saude*). |
| **Total Revenue** | X-Axis (Columns) | Derived `total` field | Composite | Continuous Numeric | Determines length of horizontal bar. Colored blue if performance exceeds the portfolio mean line; colored grey if below. |
| **Average Benchmark** | Reference Line | `AVG(Revenue per Category)` | Calculated Field | Numeric Constant | A dynamic vertical visual anchor calculating the global mean revenue across all product categories. |

### C. Geographic Market Penetration Map (Choropleth Map)
* **Visual Encoding:** Geographic Boundaries = Brazilian States, Color Saturation = Revenue Volume.
* **Target Analytical Dimension:** Regional density and concentration risk.

| UI Field Name | Mapping Axis / Role | Underlying Data Column | Source Table | Data Type | Functional Description |
|:---|:---|:---|:---|:---|:---|
| **State** | Geographic Detail | `customer_state` | `customers` | Geographic / ISO | Generates the boundaries for the filled polygon chart representing individual Brazilian federal states. |
| **Revenue Density** | Color (Mark Card) | Derived `total` field | Composite | Continuous Numeric | Controls color saturation. Darker navy indicates high-revenue hubs (e.g., SP); light ice blue indicates emerging regions. |

---
*For the underlying production scripts that generate these tabular structures, reference the `/sql` directory. For programmatic validations, reference the `/python` directory.*