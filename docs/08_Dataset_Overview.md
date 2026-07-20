# Dataset Overview

## Source

[Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle). Not redistributed in this repository due to size — download directly from Kaggle to reproduce the analysis.

## Tables Used

`orders`, `order_items`, `customers`, `products` (with `product_category_name_translation`), and `payments`. Full column-level detail: `09_Data_Model.md`.

## Granularity

The natural grain of the joined dataset is **one row per order item** — an order containing three products produces three rows in `order_items`. Every revenue KPI in this project sums line-level values rather than counting rows, to avoid overstating order counts.

## Relationships

Customers place orders (1:many); orders contain order items (1:many), each linked to one product and one seller; orders can have one or more payment records. Full ER-level detail and diagram specification: `09_Data_Model.md`.

## Data Quality

- No major missing-value issues in the core `orders`/`order_items`/`products` join for the fields used in this analysis.
- One structurally important nuance: `customer_id` is generated **per order**, while `customer_unique_id` persists across orders for the same real customer. Any repeat-purchase or retention metric must use `customer_unique_id` — see `14_Limitations.md` for how this affects interpretation of the retention finding.

## Limitations

- Time-bounded (2016–2018); does not reflect current-day Olist performance.
- Geolocation is approximate (zip-code prefix level), not exact address-level.
- Anonymized customer and seller identifiers — no demographic or firmographic enrichment is possible from this dataset alone.

Full data dictionary (column-by-column): `data_dictionary.md`.
