# Q. Which city/state generates the highest total revenue?

SELECT 
      c.customer_state,
      SUM(order_items.price + order_items.freight_value) AS total
FROM customers c
JOIN orders o 
ON o.customer_id = c.customer_id
JOIN order_items 
ON order_items.order_id = o.order_id    
GROUP BY 
        c.customer_state
ORDER BY total DESC
;      

SELECT 
      c.customer_city,
      SUM(order_items.price + order_items.freight_value) AS total
FROM customers c
JOIN orders o 
ON o.customer_id = c.customer_id
JOIN order_items 
ON order_items.order_id = o.order_id    
GROUP BY 
        c.customer_city
ORDER BY total DESC
;    

