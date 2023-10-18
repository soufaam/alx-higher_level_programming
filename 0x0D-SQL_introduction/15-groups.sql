-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score; 
