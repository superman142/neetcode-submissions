-- Write your query below
WITH temp as (
    SELECT from_id as frm, to_id as t, duration 
        FROM calls
    WHERE from_id < to_id
    UNION ALL
    SELECT to_id as frm, from_id as t, duration
        FROM calls
    WHERE to_id < from_id
)
SELECT frm as person1, t as person2, COUNT(*) as call_count, SUM(duration) as total_duration
FROM temp
GROUP BY person1, person2;