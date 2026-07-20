# Executive E-Commerce Sales Dashboard Documentation

## Overview
The `/dashboard` directory contains the visual layer of the E-Commerce Sales Analysis framework. The primary deliverable is an enterprise-grade Tableau dashboard designed to translate complex relational database queries into high-impact, interactive business insights for stakeholders, executives, and operational teams.

This visual system aligns directly with the underlying data model verified via Python and extracted via the production SQL engine.

---

## Dashboard Visual Architecture

The dashboard is structured into four core functional zones to optimize the decision-maker's cognitive workflow:

### 1. High-Level Executive Summary (KPI Tiles)
* **Location:** Top Banner
* **Metrics Displayed:**
  * **Average Order Value (AOV):** 161
  * **Total Gross Revenue:** 15,843,553
  * **Total Order Volume:** 95,420
* **Strategic Purpose:** Provides immediate operational context and high-level health tracking at a single glance.

### 2. Temporal Revenue Velocity (Line Chart)
* **Location:** Bottom-Left Quadrant
* **Component Type:** Chronological Trend Line Chart
* **Metrics Displayed:** Month-over-Month Gross Revenue distribution (January through December).
* **Strategic Purpose:** Exposes deep seasonal variations, peak sales cycles (e.g., Q2 performance peaks), and post-holiday regression patterns to guide inventory management and marketing spend allocation.

### 3. Product Portfolio Performance Matrix (Horizontal Bar Chart)
* **Location:** Bottom-Center Quadrant
* **Component Type:** Pareto-focused Horizontal Bar Chart with an embedded **Average Benchmark Line**.
* **Metrics Displayed:** Gross Revenue contribution by product category (e.g., *beleza_saude*, *relogios_presentes*, *cama_mesa_banho*).
* **Strategic Purpose:** Segregates high-value revenue drivers from long-tail underperforming segments. The integrated vertical benchmark average line allows instantaneous identification of categories operating above or below the portfolio mean.

### 4. Geographic Market Penetration Map (Choropleth Map)
* **Location:** Right Half Pane
* **Component Type:** Regional Density Choropleth Map of Brazil.
* **Metrics Displayed:** Transaction volume and revenue distribution across states.
* **Strategic Purpose:** Highlights core regional strongholds (heavily concentrated in the Southeast region, specifically São Paulo and Rio de Janeiro) and identifies market penetration risks or underserved expansion regions.

---

## Technical Specifications & Interactivity

* **Core Platform:** Tableau Desktop / Public
* **Design Guidelines Applied:** Clean typography, descriptive labels, high contrast minimal layout, and desaturated, professional slate-blue accents to prioritize data readability over decorative elements.
* **Interactivity Controls:** All visual panes function as bidirectional filters. Selecting a specific geographic state updates the category rankings and monthly trends to that region; selecting a specific product category filters the geographic distribution and monthly sales velocity.

---

## Access & Deployment

* **Static Preview Asset:** `dashboard/Olist sales dashboard.png`
* **Live Interactive Version:** [Access Tableau Public Dashboard](https://public.tableau.com/views/OlistDashboard_17723869461260/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---
*For the exact field structures utilized in these metrics, reference `dashboard/dashboard_dictionary.md`. For the backend logic, see the `/sql` directory.*