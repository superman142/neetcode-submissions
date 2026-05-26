-- Write your query below
WITH points_table AS (SELECT host_team AS team_id, 
    CASE 
        WHEN host_goals > guest_goals
            THEN 3
        WHEN host_goals = guest_goals
            THEN 1
        ELSE 0
    END as points
FROM matches
UNION ALL 
SELECT guest_team as team_id,
    CASE 
        WHEN guest_goals > host_goals
            THEN 3
        WHEN guest_goals = host_goals
            THEN 1
        ELSE 0
    END as points
FROM matches)

SELECT t.team_id, t.team_name, COALESCE(SUM(p.points), 0) as num_points
FROM teams t
LEFT JOIN points_table p ON t.team_id = p.team_id
GROUP BY t.team_id
ORDER BY num_points DESC, team_id ASC;

