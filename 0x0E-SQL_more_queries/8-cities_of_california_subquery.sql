-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
USE hbtn_0d_usa;
SELECT id, name FROM cities 
WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
