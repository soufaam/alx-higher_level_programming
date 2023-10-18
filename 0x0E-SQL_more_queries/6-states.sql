-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
CREATE   DATABASE  IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE  TABLE IF NOT EXISTS states(
	id INT,
	name VARCHAR(256)
);
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
