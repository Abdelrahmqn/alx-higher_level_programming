-- COMPUTE the average of the temperature (fahrenheit)

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city`
ORDER BY `avg_temp` DESC;