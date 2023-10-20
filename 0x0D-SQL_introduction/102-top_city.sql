-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
USE hbtn_0c_0;
SELECT temperatures.city, AVG(temperatures.value) AS avg_temp FROM temperatures
WHERE temperatures.month = 7 OR temperatures.month = 8
GROUP BY temperatures.city ORDER BY avg_temp DESC LIMIT 3;
