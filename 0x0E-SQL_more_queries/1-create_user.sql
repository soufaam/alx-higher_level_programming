-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
