-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
CREATE   DATABASE  IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (id),
	name VARCHAR(256)
);
