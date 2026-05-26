-- Write your query below

SELECT name from sales_person 
where sales_id not in
(SELECT o.sales_id from orders o
join company c on o.com_id = c.com_id
where c.name = 'CRIMSON');