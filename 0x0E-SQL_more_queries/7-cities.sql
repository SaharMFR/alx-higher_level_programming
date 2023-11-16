-- Creates the database `hbtn_06_usa` and the table `cities` with :
-- 	INT, unique, auto generated, not null and primary key -> `id`,
--	INT, not null and foreign key references to `id` of the `states` table -> `state_id`,
--	VARCHAR(256) and not null -> `name`.
-- Doesn't fail if the database or the table already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL
	);
