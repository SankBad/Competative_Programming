SELECT a.cust_name as customer_number
FROM (SELECT customer_number as cust_name, COUNT(*)
FROM orders
GROUP BY customer_number
ORDER BY 2 DESC
LIMIT 1) a
