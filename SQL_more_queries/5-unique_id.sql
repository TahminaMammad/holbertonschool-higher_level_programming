-- 5-unique_id.sql
-- Script that creates the table unique_id
-- Table description:
--   id INT with default value 1 and must be unique
--   name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
