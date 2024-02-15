-- Script that lists number of same score
SELECT score, COUNT(*) AS number
FROM second_table
ORDER BY DESC
