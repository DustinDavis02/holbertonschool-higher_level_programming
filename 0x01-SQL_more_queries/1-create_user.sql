-- Script that Creates a user user_0d_1 and gives user all privileges on the MYSQL server.
-- Creates user and sets privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';