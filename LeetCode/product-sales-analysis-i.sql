SELECT a.product_name, b.year, b.price
FROM Sales as b, Product as a
WHERE a.product_id = b.product_id
