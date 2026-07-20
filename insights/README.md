# Extracted Analytical Deliverables & Data Assets

## Overview
This directory contains the production data outputs extracted directly from the primary transaction ledger via the SQL analysis engine (`/sql`) and validated programmatically via Python (`/python`). 

These tabular deliverables represent the clean, aggregated text-based source of truth that drives the executive reporting layer and populates the visual elements within the enterprise dashboard (`/dashboard`).

---

## Data Delivery Manifest

The analytical data extracts are partitioned into four targeted business scopes:

### 1. High-Level Enterprise KPIs (`KPIS.csv`)
* **Strategic Focus:** Core global operational health indicators.
* **Schema Attributes:** `total_revenue`, `total_customers`, `AOV`
* **Baseline Verified Matrix:**
  * **Total Gross Revenue:** $15,843,553.24$
  * **Total Deduplicated Customer Base:** $95,420$
  * **Average Order Value (AOV):** $\$160.58$

### 2. Temporal Performance Distribution (`monthly.csv`)
* **Strategic Focus:** Time-series performance and fiscal seasonality profiling.
* **Schema Attributes:** `month`, `total`
* **Key Observations Supported:** Provides historical gross monthly financial records (ranging from baseline months like January at $\$1,244,490.38$ up to peaks like August at $\$1,671,513.07$) to trace baseline seasonal demand curves.

### 3. Product Portfolio Performance Rankings (`Sale by category.csv`)
* **Strategic Focus:** Revenue generation breakdown across unique product categories to guide inventory and merchandising models.
* **Schema Attributes:** `product_category_name`, `total`
* **Key Observations Supported:** Highlights market leaders across the entire product ecosystem, documenting top-tier categories such as *beleza_saude* ($\$1,441,248.07$), *relogios_presentes* ($\$1,305,541.61$), and *cama_mesa_banho* ($\$1,241,681.72$).

### 4. Regional Market Penetration Metrics (`State.csv`)
* **Strategic Focus:** Geographic revenue concentration and territorial performance mapping.
* **Schema Attributes:** `customer_state`, `total`
* **Key Observations Supported:** Quantifies regional market distribution across Brazilian federal states, highlighting core revenue hubs such as São Paulo (`SP`: $\$5,921,678.12$), Rio de Janeiro (`RJ`: $\$2,129,681.98$), and Minas Gerais (`MG`: $\$1,856,161.49$).

---

## Operational Data Integrity Enforcements
* **Transactional Scope:** Financial metrics uniformly reflect the combined baseline item cost and corresponding freight values passed to consumers ($\text{Price} + \text{Freight}$).
* **Deduplication Logic:** Customer counts are verified against unique buyer IDs (`customer_unique_id`) to prevent inflation caused by repeat order placements, providing an accurate view of market reach.
* **Downstream Integration:** These CSV extracts can be instantly imported into standard modeling tools (Excel, Python, R) or alternate BI environments to ensure data consistency across all reporting interfaces.

---
*For the underlying database syntax used to generate these extracts, see the `/sql` directory. For a complete textual analysis of these findings, see `docs/12_Business_Insights.md`.*