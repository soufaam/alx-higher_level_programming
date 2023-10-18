-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
CREATE  TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256)
);
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
