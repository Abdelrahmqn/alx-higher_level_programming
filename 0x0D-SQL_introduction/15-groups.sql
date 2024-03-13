-- list all number records in the second table.
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;