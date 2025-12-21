-- 6-states.sql
-- Script that creates the database hbtn_0d_usa and the table states
-- Table description:
--   id INT unique, auto generated, not null, primary key
--   name VARCHAR(256) not null
-- If the database or table already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
