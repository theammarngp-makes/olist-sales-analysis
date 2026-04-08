-- 	Q.	KPI Summary (Revenue, Orders, Customers, AOV)

WITH kpis AS (
    SELECT 
        o.order_id,
        c.customer_unique_id,
        SUM(oi.freight_value + oi.price) AS total
    FROM order_items oi
    JOIN orders o
        ON oi.order_id = o.order_id
    JOIN customers c
        ON c.customer_id = o.customer_id
    GROUP BY o.order_id, c.customer_unique_id
)

SELECT
    ROUND(SUM(total),2) AS total_revenue,
    COUNT(DISTINCT customer_unique_id ) AS total_customers,
    ROUND(AVG(total),2) AS AOV
FROM kpis ;

-- sum(total) for total revenue 
-- COUNT(Distinct customer_unique_id) rteurns total number of customers 
-- AVG(total) retuens avg value
