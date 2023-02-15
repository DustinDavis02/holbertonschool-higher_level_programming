-- Script that lists all records of second_table in the hbtn_0c_0 MYSQL database.
-- Lists all records of second table.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;