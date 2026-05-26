-- Write your query below
SELECT sale_date,
    SUM(
        CASE
            WHEN fruit = 'apples'
                THEN sold_num
            ELSE -1 * sold_num
        END 
    ) as diff
FROM sales
GROUP BY sale_date;