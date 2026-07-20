# Additional Deliverables — Reviews, Diagrams, Client Outlines, Perspectives, Template Roadmap, TODO

> **Access note repeated for transparency:** GitHub blocks automated crawling of individual file/blob pages, so the SQL/Python line-by-line review below is written as a **checklist of what to apply**, based on filenames and standard best practice — not a verified diff of your actual code. Paste or upload the 4 `.sql` files and the Pandas file directly in chat and I will return exact before/after code.

---

## Task 5 — SQL Review Checklist

Apply this checklist to each of `sales_kpis.sql`, `category_revenue.sql`, `monthly_revenue.sql`, `state_city_revenue.sql` (rename the fourth from `State & City wise_Revenue.sql` — spaces in filenames break some clone/CI tooling):

| Area | What to check / fix |
|---|---|
| Formatting | One clause per line (`SELECT`, `FROM`, `WHERE`, `GROUP BY` each on their own line); consistent keyword casing (all caps for SQL keywords) |
| Naming | Aliases should be meaningful (`o` for orders, `oi` for order_items — not `a`, `b`, `c`); output column aliases should be business-readable (`total_revenue`, not `SUM(price)`) |
| Comments | A one-line header comment per file stating the business question it answers (mirrors `06_Business_Questions.md`) |
| Readability | Use CTEs (`WITH revenue_by_month AS (...)`) instead of nested subqueries where more than one transformation step is involved |
| Performance | Filter (`WHERE order_status = 'delivered'`) before aggregating, not after; avoid `SELECT *` in any production-style query |
| Business logic | Confirm revenue = price + freight_value consistently across all 4 files (a common bug is summing price in one query and price+freight in another, silently producing mismatched totals) |
| Retention logic | If any query touches repeat purchases, confirm it joins on `customer_unique_id`, not `customer_id` (see `docs/09_Data_Model.md`) |

**Suggested folder ordering** (matches the methodology flow, not alphabetical):
```
sql/
├── 01_sales_kpis.sql
├── 02_monthly_revenue.sql
├── 03_category_revenue.sql
└── 04_state_city_revenue.sql
```

---

## Task 6 — Python Review Checklist

| Area | What to check / fix |
|---|---|
| Structure | Split into clear sections/cells: imports → load → clean → feature engineer → EDA → export; a notebook that mixes all five throughout is harder to audit |
| Comments | Each transformation step should state *why*, not just *what* (e.g., "translating category names from Portuguese for readability," not just "translate categories") |
| Functions | Repeated logic (e.g., computing revenue, formatting dates) should be extracted into named functions rather than repeated inline |
| Naming | Variable names should be business-readable (`monthly_revenue_df`, not `df2`) |
| Reusability | If the same cleaning steps would apply to a refreshed dataset, confirm the notebook can be re-run top-to-bottom without manual intervention (no hardcoded row indices, no hand-edited intermediate CSVs) |
| Notebook organization | Add a markdown cell at the top stating purpose and linking to `docs/10_Methodology.md`; add a markdown cell before each chart stating which business question it answers |

No working logic should be rewritten unnecessarily — this is a structure/clarity pass, not a rebuild.

---

## Task 7 — Dashboard Review

Based on the existing static screenshot and Tableau Public link (visual improvements only — no new charts invented):

| Area | Suggestion |
|---|---|
| Layout | Lead with a KPI strip (Revenue, Orders, AOV) at the top, then trend/category/region charts below — currently the PNG appears to lead with a chart rather than headline numbers |
| Business KPIs | Ensure all three headline KPIs from `docs/11_KPI_Definitions.md` are visible without scrolling |
| Visual hierarchy | One dominant chart (monthly trend) should be visually largest; category/region breakdowns can be secondary panels |
| Filters | Add a date-range and category filter if not already present, so a stakeholder can self-serve a sub-question without a new query |
| Titles | Every chart title should be a business question, not a chart type (e.g., "Which categories drive revenue?" not "Category Bar Chart") |
| Color consistency | One consistent color per category/region across all charts in the dashboard, so the same category is visually identifiable everywhere it appears |
| Executive summary section | Add a text/annotation panel at the top-left summarizing the single most important takeaway, so a viewer who never clicks a filter still leaves informed |
| Storytelling | Order panels left-to-right / top-to-bottom in the same sequence as `docs/06_Business_Questions.md`, so the dashboard reads like an answer sequence, not a grid of unrelated charts |

---

## Task 8 — Diagram Specifications (for you to render in draw.io / Lucidchart / dbdiagram.io)

### Analytics Workflow Diagram
Horizontal flow, 8 boxes, left to right:
`Business Understanding → Data Understanding → Cleaning (Python) → EDA (Python) → SQL (KPIs) → Visualization (Tableau) → Insights → Recommendations`
Use one consistent box color per phase-type: blue for understanding, green for technical processing, orange for output/story.

### Project Architecture Diagram
Three horizontal layers, top to bottom:
1. **Source layer:** Kaggle CSV export (single box)
2. **Processing layer:** two boxes side by side — "Python (cleaning/EDA)" and "SQL (KPI queries)" — with an arrow from Python to SQL if SQL runs against Python-cleaned tables, or both arrows from Source if they run independently (confirm which applies to your actual pipeline)
3. **Presentation layer:** "Tableau Dashboard" and "Markdown Documentation" side by side, both fed by the processing layer

### Data Pipeline Diagram
Same as architecture diagram but annotated with file names at each arrow (e.g., the arrow from Source to Python labeled `olist_*.csv`, the arrow from Python to SQL labeled with the cleaned table name).

### Business Process Diagram
Depicts the marketplace transaction lifecycle, not the analytics pipeline: `Seller lists product → Customer orders → Olist coordinates fulfillment → Delivery → Review survey`. Useful in `02_Business_Background.md` to orient a reader unfamiliar with Olist's model.

### Folder Structure Diagram
A simple tree (can be rendered as an actual folder-tree image or left as the markdown tree already in the README) — not worth a separate diagramming tool; the markdown tree in the README is sufficient and more maintainable.

### ER Diagram
Full specification already provided in `docs/09_Data_Model.md` — entities, keys, and cardinalities are fully defined there, ready to paste into dbdiagram.io's DBML syntax or any ER tool.

---

## Task 9 — Client Deliverable Outlines

### Executive Report (1–2 pages)
1. Headline finding (one sentence)
2. Three key insights (one paragraph each)
3. Three recommendations with owner + timeframe
4. One "ask" — what leadership needs to decide or approve

### Business Report (5–8 pages)
1. Business background & problem
2. Methodology (one paragraph, non-technical)
3. Findings by theme (growth/seasonality, concentration, retention)
4. Recommendations with prioritization logic
5. Limitations (plain-language version of `docs/14_Limitations.md`)
6. Appendix: KPI definitions

### Executive Presentation (8–10 slides)
1. Title + one-line thesis
2. Business context (background + problem)
3. Headline KPIs
4. Insight 1 (seasonality) + supporting chart
5. Insight 2 (category concentration) + supporting chart
6. Insight 3 (geographic concentration) + supporting chart
7. Insight 4 (retention) + supporting chart
8. Recommendations (short/medium/long-term, one slide)
9. Business impact framing (no invented numbers)
10. Next steps / Q&A

### Dashboard Walkthrough (script for a live or recorded demo)
1. Open on the KPI strip — "here's where the business stands overall"
2. Point to the monthly trend — "here's the pattern that explains the recent dip"
3. Filter to top category — "here's where that trend concentrates"
4. Filter to top state — "and here's where it concentrates geographically"
5. Close on the retention figure — "and here's the one lever most within our control"

---

## Task 10 — Four-Perspective Review

**Recruiter (30–60 second scan):** Sees the title, the executive summary at the top of the README, and the KPI numbers immediately. With the business-first framing now in place, a recruiter registers "this person thinks in business terms, not just query syntax" within the first screen — previously they would have seen tools before business context.

**Senior Data Analyst:** Checks whether the SQL is modular and whether the Python is reusable, then checks whether insights are actually derived from the data or just asserted. The module-mapped SQL table and the "finding → why it matters → what it implies" structure in `12_Business_Insights.md` are what a senior peer looks for to distinguish a real analyst from someone who can produce charts.

**Business Owner:** Doesn't care about SQL or Python at all — reads the Executive Summary and the Recommendations table, and wants to know one thing: is there something actionable here I can approve this quarter? The horizon-based, owner-assigned recommendation structure directly answers that.

**Analytics Consultant:** Checks whether limitations are stated honestly, whether recommendations are prioritized with logic (not just listed), and whether the deliverable would survive a client pushing back with "how confident are you in that number?" The explicit `14_Limitations.md` and the "why stating this matters" framing are what separate a consulting-grade deliverable from a student report.

---

## Task 11 — Reusable Template Roadmap (cross-industry)

The structure in this repository (`01_Executive_Summary.md` → `15_Conclusion.md`, plus `sql/`, `python/`, `dashboard/`) is already industry-agnostic — it's organized around *business decision types* (concentration risk, retention, seasonality, KPI tracking), not Olist-specific logic. To generalize it:

| Step | Action |
|---|---|
| 1 | Extract the 15-doc structure and the SQL/Python/dashboard folder pattern into a blank template repo (`analytics-case-study-template`) |
| 2 | Replace Olist-specific KPIs in `11_KPI_Definitions.md` with a placeholder table (`[Revenue metric]`, `[Volume metric]`, `[Retention metric]`) and a note on how to select the right ones per industry |
| 3 | For each target industry, note which of the four risk types (concentration, retention, seasonality, mix/pricing) map most directly: |

| Industry | Most relevant risk types from this template |
|---|---|
| Retail | Category concentration, seasonality |
| Pharmacy | Product-mix concentration, regulatory/compliance overlay (additional section needed) |
| Medical Distribution | Customer/account concentration, contract renewal (retention analog) |
| Manufacturing | Supplier/customer concentration, order-cycle seasonality |
| Clothing | Seasonality (strongest of all industries here), category concentration |
| Wholesale | Account concentration, order-frequency retention |
| FMCG | Category/SKU concentration, seasonality |
| Healthcare | Patient/payer concentration, appointment/visit retention analog |
| Finance | Product/portfolio concentration, client retention, regulatory overlay |

4. Keep the "finding → why it matters → what it implies" insight structure and the "what/why/timeframe/owner" recommendation structure exactly as-is — these are the two most reusable, industry-agnostic elements of the entire template.

---

## Task 12 — Prioritized TODO Checklist

### Critical
- [ ] Rename `State & City wise_Revenue.sql` (remove the space)
- [ ] Confirm repeat-purchase logic uses `customer_unique_id`, not `customer_id`
- [ ] Replace README with the consulting-grade version already delivered
- [ ] Add all 15 numbered docs to a `docs/` folder in the actual repo (delivered above)
- [ ] Add `docs/09_Data_Model.md`'s ER diagram as an actual rendered image (currently a spec only)

### Important
- [ ] Apply the SQL review checklist (Task 5) once you upload the actual files
- [ ] Apply the Python review checklist (Task 6) once you upload the actual notebook
- [ ] Apply dashboard layout suggestions (Task 7) in Tableau
- [ ] Add GitHub topics, a social preview image, and fix the "100% Python" language mischaracterization (see `01_AUDIT_AND_ROADMAP.md` §4)
- [ ] Cross-link the two related repos back to this one

### Nice to Have
- [ ] Render the four diagrams specified in Task 8 as actual images
- [ ] Produce the Executive Presentation outline (Task 9) as an actual slide deck
- [ ] Add a period-over-period category growth query (closes Business Question 8)

### Future Enhancements
- [ ] Forecasting model (next-quarter revenue by category/region)
- [ ] Repeat-purchase propensity model
- [ ] Power BI migration as a comparison exercise
- [ ] Live data source + scheduled refresh automation
- [ ] Generalize this repo into the cross-industry template (Task 11)
