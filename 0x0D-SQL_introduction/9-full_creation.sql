-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO  second_table(id, name, score) VALUES (89, 'John',10);
INSERT INTO  second_table(id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO  second_table(id, name, score) VALUES (3, 'BOB', 14);
INSERT INTO  second_table(id, name, score) VALUES (4, "George", 8);
