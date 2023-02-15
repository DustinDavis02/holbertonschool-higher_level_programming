-- Script that lists all records with a score >= 10 in the second_table of the hbtn_0c_0 MYSQL database.
-- Lists all records with a score >= 10.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;