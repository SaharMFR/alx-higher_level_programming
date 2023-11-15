-- Creates the table `unique_id` with INT id with dafault value 1 and must be unique, and VARCHAR(256) name.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
