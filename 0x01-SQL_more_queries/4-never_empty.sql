--  Script that Creates table id_not_null with id and name on MYSQL server.
-- Creates table with id and name
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);