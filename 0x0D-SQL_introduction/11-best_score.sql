-- only prints the 10 or later
SELECT score, name FROM second_table
where score >= 10
ORDER BY score DESC