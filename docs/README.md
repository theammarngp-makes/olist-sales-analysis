# Olist E-Commerce Revenue & Retention Analysis
**A revenue diagnostics engagement for a Brazilian multi-category marketplace**

[Live Dashboard](https://public.tableau.com/views/OlistDashboard_17723869461260/Dashboard2) · [SQL](./sql) · [Python](./python) · [Data Dictionary](./docs/data_dictionary.md) · [Recommendations](./docs/recommendations.md)

---

## Executive Summary

Olist, a Brazilian marketplace connecting small and medium merchants to consumers nationwide, generated **R$15.8M** in revenue across **95,420 orders** (AOV: **R$161**) in the analyzed period. Growth was strong through mid-year before flattening, revenue is concentrated in a small number of states and product categories, and the large majority of customers purchase only once.

This engagement traces that performance from raw order data through SQL-based KPI extraction, exploratory analysis in Python, and an interactive Tableau dashboard — and turns the findings into a prioritized set of business recommendations, not just a chart pack.

**Bottom line:** Olist's near-term growth is more exposed to concentration risk (a few states, a few categories) and repeat-purchase weakness than to demand — both are addressable without new markets or new inventory.

---

## Business Background

Olist operates a marketplace model: it does not sell its own inventory but connects independent sellers across Brazil to buyers on major online retail channels. Revenue depends on transaction volume across many small merchants rather than a concentrated set of large accounts, which makes category mix, regional distribution, and repeat engagement structurally important to the business — unlike a single-brand retailer, Olist's growth is a function of how broad and repeatable its marketplace activity is.

## Business Problem

Leadership currently has visibility into top-line revenue but limited structured visibility into:
- Which categories and regions are actually driving growth vs. riding overall momentum
- Whether the customer base is being retained or constantly replaced
- Where revenue is concentrated enough to represent a single point of failure

Without this, marketing spend, regional expansion, and retention investment are being made on intuition rather than evidence.

## Business Objectives vs. Technical Objectives

| Business Objectives | Technical Objectives |
|---|---|
| Identify where revenue is at risk of concentration | Build reusable SQL KPI queries against the Olist schema |
| Find the highest-leverage retention opportunity | Engineer clean, join-ready tables in Python |
| Give category/regional teams a shared source of truth | Deliver an interactive, filterable Tableau dashboard |
| Prioritize 3 recommendations leadership can act on this quarter | Document methodology so the analysis is auditable and repeatable |

## Stakeholders

| Stakeholder | What they need from this analysis |
|---|---|
| CEO | Is growth durable, and where's the exposure? |
| Sales Manager | Which categories/regions to prioritize this quarter |
| Marketing | Where to spend to convert one-time buyers into repeat buyers |
| Finance | Revenue concentration risk for forecasting |
| Operations | Order volume patterns for staffing/capacity |
| Supply Chain | Which categories/regions need inventory attention |
| Customer Success | Where retention is weakest |

## Business Questions

1. What is total revenue, order volume, and AOV, and how have they trended month over month?
2. Which product categories generate the majority of revenue (Pareto concentration)?
3. Which states/regions contribute the most and least revenue?
4. Is revenue growth being driven by new customers, repeat customers, or both?
5. What percentage of customers are repeat purchasers?
6. How does AOV vary by category and by region?
7. Is there a seasonal pattern to order volume, and when does it peak/trough?
8. Which categories are growing vs. declining relative to the prior period?
9. How exposed is total revenue to underperformance in the top 3 states?
10. How exposed is total revenue to underperformance in the top 3 categories?
11. What is the average order value trend over time, and is it rising or falling independent of volume?
12. Are there categories with high order volume but low revenue contribution (low-value, high-frequency)?
13. Which regions are under-represented relative to population and could be under-penetrated?
14. What does the order-volume-to-revenue ratio suggest about pricing across categories?
15. What is the month with the single highest order volume, and what preceded it?
16. Where should marketing budget move first based on category concentration?
17. What would a 10% improvement in repeat-purchase rate mean directionally for order volume?
18. Which KPIs should leadership track monthly vs. quarterly?
19. What data quality issues, if any, limit confidence in category or regional figures?
20. What is the minimum viable retention initiative that addresses the biggest identified gap?

*(See `docs/business_questions.md` for the full list with answers and supporting query references.)*

## Dataset Overview

- **Source:** [Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)
- **Granularity:** One row per order item, joinable up to order → customer → product → seller → review level
- **Core tables used:** orders, order_items, products, customers, payments
- **Relationships:** Orders link to customers (1:1 per order), order_items link many-to-one to orders and products, payments link many-to-one to orders
- **Limitations:** Dataset is anonymized and time-bounded (2016–2018); customer identifiers reset per order in the public release, so "repeat purchase" figures reflect the dataset's customer-linking convention, not necessarily Olist's live CRM identity — noted wherever repeat-purchase metrics are used
- Full dictionary: `docs/data_dictionary.md`

## Data Quality Assessment

Documented in `docs/data_quality_assessment.md` — see especially the note on customer-ID granularity above, which affects any repeat-purchase interpretation and should be read before citing that KPI externally.

## Data Preparation

Cleaning and feature engineering (category translation, revenue rollups, date parsing, state-level aggregation) is handled in `python/` — see that folder's own README for a step-by-step account of every transformation applied before the SQL layer runs.

## Methodology

```
Business Understanding
        ↓
Data Understanding (schema, relationships, quality)
        ↓
Cleaning & Feature Engineering (Python)
        ↓
Exploratory Data Analysis (Python)
        ↓
KPI & Business-Question SQL (sql/)
        ↓
Visualization (Tableau)
        ↓
Insights
        ↓
Recommendations
```

## Exploratory Data Analysis

Full notebook walkthrough in `python/`. Every chart there is tied to one of the business questions above rather than produced as a generic EDA pass.

## SQL Analytics

| File | Business Module | Answers |
|---|---|---|
| `sql/sales_kpis.sql` | Core KPIs | Revenue, orders, AOV |
| `sql/category_revenue.sql` | Product | Category-level revenue concentration |
| `sql/monthly_revenue.sql` | Time | Monthly trend and seasonality |
| `sql/state_city_revenue.sql` | Regional | State/city revenue distribution |

*(Filenames above reflect the recommended rename from `01_AUDIT_AND_ROADMAP.md` §4 — update paths once renamed in the repo.)*

## Python Analytics

Purpose, cleaning steps, feature engineering, and every visualization are documented inline in `python/README.md`, cross-referenced to the business questions they answer.

## KPI Library

| KPI | Formula | Business Importance | Decision Supported |
|---|---|---|---|
| Total Revenue | Σ(order item price + freight) | Top-line health | Growth forecasting |
| Total Orders | COUNT(distinct order_id) | Volume/demand signal | Ops/staffing planning |
| AOV | Total Revenue ÷ Total Orders | Pricing & basket health | Pricing/promotion decisions |
| Category Revenue Share | Category Revenue ÷ Total Revenue | Concentration risk | Marketing/inventory prioritization |
| State Revenue Share | State Revenue ÷ Total Revenue | Geographic risk | Regional expansion decisions |
| Repeat Purchase Rate | Customers with 2+ orders ÷ Total Customers | Retention health | Retention program investment |

Full version with edge cases and caveats: `docs/kpi_library.md`

## Dashboard

**Audience:** Sales, Marketing, and Executive leadership
**Purpose:** Self-serve view of revenue trend, category mix, and regional distribution without needing to run SQL
**Decisions supported:** Category prioritization, regional budget allocation, monthly performance review

[View Interactive Dashboard](https://public.tableau.com/views/OlistDashboard_17723869461260/Dashboard2)

![Dashboard overview](./dashboard/olist_dashboard.png)

## Key Insights

1. **Growth has a ceiling under current conditions.** Revenue climbed steadily through mid-year, then plateaued and declined — consistent with a seasonal ceiling rather than a demand collapse, meaning the plateau is likely to recur unscheduled unless addressed before the next cycle.
2. **The business is running a concentrated bet, not a diversified one.** A small share of categories generates the majority of revenue — that's efficient today, but it means a single category's decline moves the whole top line.
3. **Geographic revenue is similarly concentrated**, which functions as an unhedged regional dependency: a disruption (logistics, competition, local economic shift) in the top state has an outsized effect on total revenue.
4. **Retention, not acquisition, is the weakest link.** The majority of customers buy once and do not return — meaning current revenue is substantially a function of new-customer acquisition, which is a more expensive and less durable growth lever than repeat engagement.

## Business Recommendations

**Short-term (0–3 months)**
- Launch a targeted repeat-purchase campaign (email/retargeting) aimed at recent one-time buyers — directly addresses Insight 4, the lowest-cost lever available.

**Medium-term (3–6 months)**
- Build a category-diversification watchlist: identify 2–3 adjacent categories with growth potential to reduce Pareto concentration (Insight 2).
- Pilot regional marketing spend in one under-penetrated state to test whether geographic concentration is a demand ceiling or a marketing-spend gap (Insight 3).

**Long-term (6–12 months)**
- Establish a recurring monthly KPI review (this dashboard) as the standing source of truth for category and regional performance, replacing ad hoc reporting.

*(Prioritization logic and ownership: `docs/recommendations.md`)*

## Business Impact

These recommendations do not claim a specific revenue lift — no financial projection is invented here. What they do is convert three qualitative risks (seasonality, concentration, retention) into concrete, ownable initiatives with a defined time horizon, so leadership can decide funding and track progress against the same KPIs used in this analysis.

## Technical Architecture

```
Kaggle CSV Export
      ↓
Python (cleaning, feature engineering, EDA)
      ↓
SQL (KPI + business-question queries)
      ↓
Tableau Public (interactive dashboard)
      ↓
Markdown documentation (this repo)
```

## Repository Structure

```
olist-sales-analysis/
├── README.md                  ← you are here
├── LICENSE
├── docs/
│   ├── executive_summary.md
│   ├── business_background.md
│   ├── business_problem.md
│   ├── business_questions.md
│   ├── data_dictionary.md
│   ├── data_quality_assessment.md
│   ├── methodology.md
│   ├── kpi_library.md
│   └── recommendations.md
├── sql/
│   ├── sales_kpis.sql
│   ├── category_revenue.sql
│   ├── monthly_revenue.sql
│   └── state_city_revenue.sql
├── python/
│   ├── README.md
│   └── (cleaning + EDA notebook/scripts)
├── insights/
│   ├── kpis.csv
│   ├── sales_by_category.csv
│   ├── state.csv
│   └── monthly.csv
└── dashboard/
    └── olist_dashboard.png
```

## Technical Skills Demonstrated

SQL (aggregation, joins, business-question query design) · Python/Pandas (cleaning, feature engineering, EDA) · Tableau (interactive dashboard design) · Git/GitHub (structured repository documentation) · Business analytics translation (insights → prioritized recommendations)

## Future Improvements

- Forecasting next-quarter revenue by category/region
- A repeat-purchase propensity model to target retention spend
- Migrating the dashboard layer to Power BI as a comparison exercise
- Lightweight automation (scheduled refresh) if migrated to a live data source

## Related Projects

This is the first of a three-part Olist analytics series:
- [Cohort Retention Analysis](https://github.com/theammarngp-makes/E-commerce-cohort-retention-analysis) — deep dive on the retention gap flagged in Insight 4
- [RFM Customer Segmentation](https://github.com/theammarngp-makes/ecommerce-rfm-customer-segmentation) — segment-level detail behind the "repeat vs. one-time" finding above

## Author

**Mohammad Ammar**
Data Analyst — SQL · Python · Tableau · Business Analytics
[LinkedIn](https://www.linkedin.com/in/mohammad-ammar-ngp/) · [GitHub](https://github.com/theammarngp-makes)

## Dataset Source

Dataset not included due to size; download from [Kaggle: Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

## License

MIT — see `LICENSE`.
