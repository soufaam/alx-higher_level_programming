-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
USE hbtn_0c_0;
SELECT temperatures.city, AVG(temperatures.value) AS avg_temp FROM temperatures
GROUP BY temperatures.city ORDER BY avg_temp DESC;
