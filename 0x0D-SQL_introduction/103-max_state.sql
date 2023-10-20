-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
USE hbtn_0c_0;
SELECT temperatures.state, MAX(temperatures.value) FROM temperatures
GROUP BY temperatures.state ORDER BY temperatures.state ASC;
