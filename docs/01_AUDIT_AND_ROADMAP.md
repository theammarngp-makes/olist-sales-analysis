# Repository Audit & Redesign Roadmap
### Repo: `theammarngp-makes/olist-sales-analysis`
### Prepared as a consulting-style repository review

> **Scope note:** This audit is based on the repository's landing page, folder listing, README content, file names, and linked Tableau dashboard — GitHub blocks automated access to individual file pages, so the SQL and Pandas code itself was evaluated by name/structure, not line-by-line. Section 13 flags exactly what still needs a human (or an in-chat file upload) pass.

---

## 1. What's Currently There

| Item | Detail |
|---|---|
| Folders | `Pandas/`, `dashboard/`, `insights/`, `sql/` |
| Root files | `Insights.md`, `LICENSE` (MIT), `README.md` |
| SQL files | `Category_Revenue.sql`, `Monthly_Revenue.sql`, `Sales_KPIS.sql`, `State & City wise_Revenue.sql` |
| Insight exports | `KPIS.csv`, `Sale by category.csv`, `State.csv`, `monthly.csv` |
| Dashboard | One static PNG + a live Tableau Public link |
| KPIs reported | Revenue R$15.8M, 95,420 orders, AOV R$161 |
| Insights | Seasonality, category Pareto effect, state concentration risk, low repeat-purchase rate |
| Recommendations | 4 one-line bullets (marketing focus, retention, regional expansion, category optimization) |
| Author/contact | Name, LinkedIn, GitHub, 2 related repos |
| Stars/Forks | 2 / 0 — essentially undiscovered |

**Read as a whole:** this is a competent, honest, small-scope SQL+Tableau project. It reads as "I did an EDA and built a dashboard," not "I ran a consulting engagement." That's the entire gap to close — the underlying work doesn't need to change, the *framing, depth, and documentation* do.

---

## 2. Scored Evaluation (1–10)

| Category | Score | Why |
|---|---|---|
| Repository structure | 4/10 | Flat, no `docs/`, no `data/`, folder names have inconsistent casing (`Pandas` vs lowercase others), space in a filename (`State & City wise_Revenue.sql`) |
| Documentation | 3/10 | One README does all the work; no data dictionary, no methodology doc, no KPI definitions |
| Business storytelling | 3/10 | Jumps straight to charts/KPIs — no stated business, stakeholders, or decisions at stake |
| Analytics depth | 5/10 | Revenue/category/state/time covered; no cohort, retention, or window-function analysis *visible from the README* |
| SQL quality | Unscored (see §13) | Only filenames known; can't verify style, comments, or performance |
| Python quality | Unscored (see §13) | `Pandas/` folder exists but content unseen |
| Dashboard design | 5/10 | Single static PNG shown inline (large, unstyled) + Tableau Public link; no explanation of what each dashboard element supports |
| Business insights | 4/10 | Real findings, but written as observations ("revenue shows growth then decline") rather than decision-ready consulting insights |
| Recommendations | 3/10 | Four generic bullets, no timeframe, no prioritization, no owner |
| GitHub presentation | 3/10 | No topics beyond defaults, no social preview image, no badges beyond tech-stack shields, repo language shows "100% Python" which undersells the SQL work |
| Professionalism | 4/10 | Friendly and honest, but emoji-heavy headers and "Aspiring Data Analyst" framing undercut authority |
| Portfolio value | 4/10 | Useful evidence of SQL+Tableau skill, but indistinguishable from dozens of other public Olist notebooks |
| Recruiter appeal | 4/10 | A recruiter gets the KPIs in 10 seconds but nothing that signals business judgment |
| Client appeal | 2/10 | No business framing at all — a business owner has no reason to trust this over a raw dashboard |

**Composite: ~3.7/10** — solid raw material, consulting layer missing entirely.

---

## 3. Why This Matters (the core problem)

Every recruiter-facing analytics repo on GitHub has "Revenue," "Top categories," "Regional sales." What's rare — and what actually gets attention — is a repo that reads like **a memo to a CEO**, where the SQL and dashboard are *evidence*, not the product. Right now the repo leads with the dashboard; it should lead with the business problem and end with the dashboard as proof.

---

## 4. Improvement Roadmap (prioritized)

**Phase 1 — Narrative layer (highest ROI, no code changes)**
1. Rewrite README around a business case, not a tool list (see new README delivered separately).
2. Add `docs/01_executive_summary.md` through `docs/09_business_recommendations.md` (structure below).
3. Fix the filename with a space (`State & City wise_Revenue.sql` → `state_city_revenue.sql`) — spaces in filenames break clone/CI workflows on some systems.
4. Standardize folder casing to lowercase (`Pandas/` → `python/`).

**Phase 2 — Documentation depth**
5. Add a data dictionary (`docs/data_dictionary.md`) — even a good-faith one built from the public Olist schema, to be verified against your actual tables.
6. Add a KPI library with formulas, not just values.
7. Rewrite `Insights.md` recommendations with short/medium/long-term horizons and stated business impact — no invented numbers.

**Phase 3 — Presentation & discoverability**
8. Replace the single large PNG with a cropped, captioned dashboard walkthrough (2–3 annotated views instead of one raw screenshot).
9. Add GitHub topics: `business-intelligence`, `sql-analytics`, `tableau`, `ecommerce-analytics`, `kpi-dashboard`.
10. Add a social preview image (1280×640) instead of relying on the default OG card.
11. Fix repo "Languages" mischaracterization — GitHub is showing 100% Python because `.sql` files may not be getting linted as SQL, or the Pandas folder dominates by byte count; add a `.gitattributes` if you want SQL correctly represented.

**Phase 4 — Analytical additions (optional, only if you're willing to extend the analysis — README says don't change core analysis, so treat these as *additive*, non-destructive extensions)**
12. Add one window-function-based query (e.g., month-over-month revenue with `LAG()`) to the `sql/` folder as `growth_rate.sql` — extends, doesn't replace.
13. Cross-link this repo with your two related repos *both ways* (the cohort and RFM repos should link back here too) so a recruiter sees a connected body of work, not three disconnected projects.

---

## 5. Missing Documents (to add)
- `docs/executive_summary.md`
- `docs/business_background.md`
- `docs/business_problem.md`
- `docs/business_questions.md` (15–25 questions)
- `docs/data_dictionary.md`
- `docs/data_quality_assessment.md`
- `docs/methodology.md`
- `docs/kpi_library.md`
- `docs/recommendations.md`
- `docs/architecture.md` (simple data-flow diagram: raw CSV → SQL → Python → Tableau)

## 6. Missing Analyses (candidates, additive only)
- Month-over-month / YoY growth rate via window functions
- New vs. repeat customer revenue split
- Delivery-time vs. review-score relationship (Olist dataset supports this natively)
- Payment-method mix and its relationship to AOV

## 7. Missing KPIs (candidates)
- Repeat Purchase Rate
- Revenue Concentration (% of revenue from top 3 states/categories)
- Average Delivery Time vs. Estimate
- Customer Lifetime Value (simple, order-count-based proxy — label clearly as an approximation)

## 8. Missing Business Questions (examples to seed the 15–25 list)
- Which product categories are growing vs. declining quarter over quarter?
- What is Olist's exposure if its top state underperforms next quarter?
- Does delivery delay correlate with review score, and by how much?
- What share of revenue comes from repeat customers vs. one-time buyers?
- Which regions are under-penetrated relative to population/purchasing power?

## 9. Missing Recommendations Structure
Every recommendation should carry: **what**, **why (linked to an insight)**, **timeframe**, **who owns it**. See `docs/recommendations.md` template in the new README package.

## 10. GitHub-Level Improvements
- Add topics (listed above)
- Add a social preview image
- Pin this repo + the two related ones together on your profile
- Turn on "Discussions" or at least keep Issues open — signals an active, maintained project
- Add a `CONTRIBUTING.md` only if you want outside engagement (optional, low priority for a solo portfolio piece)

## 11. Portfolio-Level Improvements
- Position this as the "flagship" of a 3-repo Olist series (this + cohort + RFM), and say so explicitly in each README
- Add one paragraph in the About/bio section stating your specialization (e.g., "e-commerce and retail analytics") rather than a generic tool list

## 12. Recruiter Review (as if scanning for 90 seconds)
A recruiter opens this repo, sees the title, and by second 15 needs: (1) what business problem, (2) what was found, (3) what tools. Currently they get tools first, insights third, business problem never. **Fix: lead the README with a 4-line "Business Context" block before anything else** — done in the new README.

## 13. What Still Needs Your Input / A Deeper Pass
Because I couldn't open the actual code files, I could not verify or improve:
- SQL formatting, comments, CTE usage, indexing logic in the 4 `.sql` files
- Whether the Pandas notebook/script does real cleaning/feature engineering or just plotting
- Actual dashboard interactivity (filters, tooltips, drill-downs) beyond what the static PNG shows

**Recommendation:** upload the 4 SQL files and the Pandas file directly in a follow-up message and I'll do a real code-quality pass (formatting, window functions, query modularization) — that closes the one gap this audit can't.
