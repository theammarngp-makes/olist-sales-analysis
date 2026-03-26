# Q. What is the monthly/yearly revenue trend?

SELECT 
      DATE_FORMAT(o.order_purchase_timestamp,"%M") as month,
      SUM(oi.price + oi.freight_value) AS total
FROM orders o 
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY 
        month
ORDER BY month
 ; 

