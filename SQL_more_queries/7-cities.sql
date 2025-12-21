-- 7-cities.sql
-- Script that creates the database hbtn_0d_usa and the table cities
-- Table description:
--   id INT unique, auto generated, not null, primary key
--   state_id INT not null, foreign key referencing states(id)
--   name VARCHAR(256) not null
-- If the database or table already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
