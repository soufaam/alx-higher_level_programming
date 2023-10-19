-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
use hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
MODIFY id INT(11);
SHOW CREATE TABLE first_table;
/home/soufiane/alx-higher_level_programming/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql