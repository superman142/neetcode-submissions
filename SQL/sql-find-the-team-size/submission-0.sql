-- Write your query below
SELECT employee_id, count(*) over (partition by team_id) as team_size from employee;