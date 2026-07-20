# Limitations

Stated explicitly and upfront, so no claim in this repository is read as more certain than it actually is.

## Data Limitations

- **Time-bounded dataset (2016–2018):** findings describe that historical window, not current Olist performance. Any external claim about "current" state should be re-verified against live data.
- **`customer_id` vs `customer_unique_id`:** the public dataset generates a new `customer_id` per order; retention/repeat-purchase figures are only valid when computed against `customer_unique_id`. If the existing SQL uses the wrong key, the repeat-purchase finding should be re-verified before being cited externally (flagged in `09_Data_Model.md`).
- **Geolocation is approximate:** zip-code-prefix level, not exact address — state/city-level conclusions are reliable, hyper-local ones are not.
- **No demographic or firmographic enrichment:** the anonymized dataset does not support customer segmentation beyond purchase behavior and location.

## Analytical Limitations

- **No period-over-period category growth query yet exists** in `sql/` — the "growing vs. declining category" question (`06_Business_Questions.md`, Q8) is currently open, not answered.
- **No external benchmark data** (population, competitor share) is included, so "under-penetrated region" claims are directional, not quantified.
- **No financial impact is projected** for any recommendation. Estimating a dollar impact of, say, a 10% retention improvement would require assumptions (campaign response rate, incremental margin) not supported by this dataset alone — stating a number here would be a fabricated confidence level, not an insight, so it is deliberately left as a scenario question in `06_Business_Questions.md` rather than answered.

## Scope Limitations

- This is a diagnostic and recommendation-generation exercise, not an implementation plan — see `07_Project_Scope.md` for what is explicitly out of scope this phase (forecasting, ML, live data integration).

## Why stating this matters

A consulting deliverable that overstates its own certainty is a liability to whoever acts on it. Every limitation above is listed so a reader — recruiter, hiring manager, or an actual business stakeholder — can calibrate exactly how much weight to put on each finding.
