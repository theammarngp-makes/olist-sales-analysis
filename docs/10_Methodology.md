# Methodology

## Workflow

```
Business Understanding
        ↓
Data Understanding (schema, relationships, quality — see 08_Dataset_Overview.md, 09_Data_Model.md)
        ↓
Cleaning & Feature Engineering (Python — category translation, date parsing, revenue rollups)
        ↓
Exploratory Data Analysis (Python — every chart tied to a question in 06_Business_Questions.md)
        ↓
KPI & Business-Question SQL (sql/ — organized by business module)
        ↓
Visualization (Tableau — interactive dashboard for stakeholder self-service)
        ↓
Insights (12_Business_Insights.md)
        ↓
Recommendations (13_Business_Recommendations.md)
```

## Why this order

Business understanding comes first deliberately — every downstream step (which columns matter, which KPIs to build, which chart to make) is a consequence of the business questions in `06_Business_Questions.md`, not the other way around. This avoids the common failure mode of "explore the data, then retrofit a business story to whatever was found."

## Tooling by Stage

| Stage | Tool | Why |
|---|---|---|
| Cleaning & feature engineering | Python / Pandas | Flexible for joins, category translation, and reusable transformation functions |
| KPI & business-question queries | SQL | Set-based aggregation is the natural fit for revenue/order rollups, and SQL is directly portable to a production warehouse |
| Visualization | Tableau | Interactive filtering for non-technical stakeholders without requiring them to run code |
| Documentation | Markdown | Version-controlled alongside the analysis, auditable in the same repository |

## Reproducibility

Anyone can reproduce this analysis by: (1) downloading the Olist dataset from Kaggle, (2) running the Python cleaning steps documented in `python/README.md`, (3) running the SQL queries in `sql/` against the cleaned tables, (4) opening the Tableau workbook or live dashboard link. No step depends on undocumented manual work.
