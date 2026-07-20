# Business Questions

Each question below is tied to the query or artifact that answers it, so the analysis stays auditable — anyone can trace a claim in the README back to the exact source.

| # | Question | Answered by | Status |
|---|---|---|---|
| 1 | What is total revenue, order volume, and AOV, and how have they trended month over month? | `sql/monthly_revenue.sql`, `insights/monthly.csv` | Answered |
| 2 | Which product categories generate the majority of revenue (Pareto concentration)? | `sql/category_revenue.sql`, `insights/sales_by_category.csv` | Answered |
| 3 | Which states/regions contribute the most and least revenue? | `sql/state_city_revenue.sql`, `insights/state.csv` | Answered |
| 4 | Is revenue growth driven by new customers, repeat customers, or both? | Requires customer-order join not currently in `sql/` | Open — see Future Improvements |
| 5 | What percentage of customers are repeat purchasers? | Referenced qualitatively in `Insights.md`; not yet a standalone query | Partially answered — recommend adding `sql/repeat_purchase_rate.sql` |
| 6 | How does AOV vary by category and by region? | Derivable from `category_revenue.sql` + `state_city_revenue.sql` combined with order counts | Answered (combine two queries) |
| 7 | Is there a seasonal pattern to order volume, and when does it peak/trough? | `sql/monthly_revenue.sql` | Answered |
| 8 | Which categories are growing vs. declining relative to the prior period? | Not yet queried — needs period-over-period comparison | Open |
| 9 | How exposed is total revenue to underperformance in the top 3 states? | Derivable from `state_city_revenue.sql` (sum top 3 ÷ total) | Answered (manual calc from existing output) |
| 10 | How exposed is total revenue to underperformance in the top 3 categories? | Derivable from `category_revenue.sql` | Answered (manual calc from existing output) |
| 11 | What is the AOV trend over time, independent of volume? | `sql/monthly_revenue.sql` if AOV column included | Check — confirm query outputs AOV, not just revenue/orders |
| 12 | Are there high-volume, low-revenue categories (low-value, high-frequency)? | `sql/category_revenue.sql` | Answered |
| 13 | Which regions are under-represented relative to population and could be under-penetrated? | Requires external population data — not in current dataset | Open |
| 14 | What does the order-volume-to-revenue ratio suggest about category pricing? | Derivable from `category_revenue.sql` | Answered |
| 15 | What is the single highest-volume month, and what preceded it? | `sql/monthly_revenue.sql` | Answered |
| 16 | Where should marketing budget move first based on category concentration? | Insight synthesis in `Insights.md` / README | Answered (qualitative) |
| 17 | What would a 10% improvement in repeat-purchase rate mean directionally? | Not modeled — flagged as a scenario exercise, not a hard projection | Open by design (avoids invented figures) |
| 18 | Which KPIs should leadership track monthly vs. quarterly? | `docs/kpi_library.md` | Answered |
| 19 | What data quality issues limit confidence in category or regional figures? | `docs/data_quality_assessment.md` | Answered |
| 20 | What is the minimum viable retention initiative addressing the biggest gap? | `docs/recommendations.md` | Answered |

**Note on "Open" items:** these are genuine gaps, listed honestly rather than glossed over — closing them (customer-level joins, period-over-period category comparison, external population benchmarks) is exactly what the "Future Improvements" section of the README describes as next-phase work, and is also visible in the two related repos (cohort retention, RFM segmentation) which pick up several of these directly.
