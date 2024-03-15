-- COMPUTE the average of the temperature (fahrenheit)

USE `hbtn_0c_0`
SELECT city, AVG(value * (9/5) + 32) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC