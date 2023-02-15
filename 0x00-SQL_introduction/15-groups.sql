-- Script that lists the numbers of records with the same score in second_table from the hbtn_0c_0 MYSQL database.
-- Lists all numbers of records with the same score.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;