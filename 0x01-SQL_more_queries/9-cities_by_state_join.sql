-- Script that lists all cities in database hbtn_0d_usa in MYSQL server.
-- lists all cities in database.
SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;