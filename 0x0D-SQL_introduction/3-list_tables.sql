-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
SET @arg1 = ?;
-- Connect to DB
USE @arg1;
-- List TAbles
SHOW TABLE;
