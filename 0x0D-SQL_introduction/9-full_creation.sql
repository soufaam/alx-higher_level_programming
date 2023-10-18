-- script database mysql
-- Set a placeholder ofthe argument MySQL server.
CREATE TABLE second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO  second_table(id, name, score) 
VALUES
(89, 'John',10),
(2, 'Alex', 3),
(3, 'BOB', 14),
(4, "George", 8);
