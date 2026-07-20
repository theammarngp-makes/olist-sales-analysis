# Q. Which product category generates the highest revenue?

SELECT p.product_category_name,
       SUM(oi.price + oi.freight_value) as total 
FROM products p
JOIN order_items oi
       ON (p.product_id=oi.product_id) 
GROUP BY p.product_category_name
order by total 
DESC  ;  
