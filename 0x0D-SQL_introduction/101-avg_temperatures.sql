-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
use hbtn_0c_0;
SELECT temperatures.city, AVG(temperatures.value) as avg_temp from temperatures
GROUP BY temperatures.city ORDER BY avg_temp DESC;
