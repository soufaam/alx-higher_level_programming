-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
-- INSERT VALUES in second_table
INSERT INTO  second_table(id, name, score) VALUES (1, 'John',10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, "George", 8);
