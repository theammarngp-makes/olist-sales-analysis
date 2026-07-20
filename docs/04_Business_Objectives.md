# Business Objectives

## Business Objectives

1. Identify where revenue is structurally concentrated (category and region) and quantify the exposure.
2. Determine whether growth is being driven by new-customer acquisition, repeat purchasing, or both.
3. Establish a documented, recurring seasonal pattern that Operations and Marketing can plan around instead of reacting to.
4. Deliver three prioritized, ownable recommendations leadership can fund and track this quarter — not a general list of observations.

## Technical Objectives

1. Build modular SQL queries against the Olist schema, organized by business module (KPIs, category, time, region), so each query answers one specific business question and can be re-run independently.
2. Perform cleaning and feature engineering in Python (category translation, date parsing, revenue rollups) that is documented step by step and reproducible.
3. Produce an interactive Tableau dashboard that lets non-technical stakeholders self-serve the same figures without needing to run SQL.
4. Document methodology, KPI definitions, and data lineage so the analysis is auditable by someone who did not build it.

## How These Connect

Every technical objective exists to serve a business objective — the SQL modules exist so leadership objectives 1–2 can be verified independently, the dashboard exists so objective 3 can be monitored without analyst involvement, and the documentation exists so objective 4's recommendations can be traced back to evidence rather than asserted.
