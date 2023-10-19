-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
SELECT cities.id, cities.name, states.name FROM cities 
LEFT JOIN states
ON cities.state_id = states.id ORDER BY cities.id ASC;
