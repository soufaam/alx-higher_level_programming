-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
SELECT score, name  FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
