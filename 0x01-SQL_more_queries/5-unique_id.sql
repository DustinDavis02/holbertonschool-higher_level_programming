-- Script that creates table unique_id with id and name on MYSQL server.
-- Creates table with id and name.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);