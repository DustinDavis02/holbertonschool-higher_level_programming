-- Script that lists all cities of california in hbtn_0d_usa MYSQL database.
-- Lists all cities of california.
SELECT id, name
  FROM cities
 WHERE state_id = (SELECT id FROM states WHERE name = "California") GROUP BY id ORDER BY id ASC;