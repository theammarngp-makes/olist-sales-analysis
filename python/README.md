# Python Analytics & Exploratory Data Analysis (EDA)

## Overview
This directory contains the foundational Python scripting utilized for the initial data ingestion, structural validation, and exploratory data analysis (EDA) of the Olist e-commerce dataset. 

The primary script (`EDA.py`) serves as the core engine for merging disparate raw data tables, establishing the initial data model, and validating the primary Business KPIs prior to SQL extraction and Tableau visualization.

## Directory Contents

| File | Purpose |
|------|---------|
| `EDA.py` | Executable script for data merging, KPI validation, and diagnostic analysis. |

## Key Analytical Workflows

The `EDA.py` script executes the following sequential operations:

1. **Data Ingestion & Integration:** 
   - Loads raw CSV extracts (Customers, Geolocation, Order Items, Payments, Orders, Products).
   - Executes structural left-joins on primary and foreign keys (`customer_id`, `order_id`, `product_id`) to create a unified analytical dataframe.
   - Derives composite metrics (e.g., `total` = `freight_value` + `price`).

2. **KPI Validation:**
   - Computes baseline programmatic metrics to ensure data integrity before database insertion.
   - Validates baseline KPIs: **Total Revenue**, **Total Orders**, **Total Customers**, and **Average Order Value (AOV)**.

3. **Diagnostic Analytics:**
   - **Product Performance:** Ranks the Top 10 products and aggregates revenue by product category.
   - **Logistics Impact Analysis:** Calculates delivery discrepancies by computing the delta between `order_estimated_delivery_date` and `order_delivered_customer_date` to isolate delayed orders.

4. **Programmatic Visualization:**
   - Generates ad-hoc `matplotlib` visualizations (e.g., Top 10 Categories by Revenue) for rapid exploratory assessment.

## Prerequisites & Execution

**1. Environment Setup**
Ensure all dependencies are installed via the root requirements file:
```bash
pip install -r ../requirements.txt

**2. Data Requirements
The script expects the raw Olist datasets to be housed in an Ecommerce Sales/ directory at the execution root. Ensure the following files are present:
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv

**3. Execution
To run the exploratory analysis pipeline:
``` bash
python EDA.py
