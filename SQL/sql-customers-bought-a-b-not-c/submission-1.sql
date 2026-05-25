-- Write your query below
SELECT customer_id, customer_name FROM customers
WHERE customer_id in (SELECT customer_id FROM orders where product_name= 'A')
AND customer_id in (SELECT customer_id FROM orders where product_name= 'B')
AND customer_id NOT IN (SELECT customer_id FROM orders where product_name= 'C')
order by customer_name;