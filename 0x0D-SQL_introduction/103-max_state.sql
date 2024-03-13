-- script 20
-- script displays max temperature of each state
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
