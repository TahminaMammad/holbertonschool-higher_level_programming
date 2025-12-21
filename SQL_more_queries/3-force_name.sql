-- 3-force_name.sql
-- Script that creates the table force_name
-- Table description:
--   id INT
--   name VARCHAR(256) NOT NULL
-- The database name will be passed as an argument of the mysql command
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
