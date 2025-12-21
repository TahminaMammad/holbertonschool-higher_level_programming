-- 8-cities_of_california_subquery.sql
-- Script that lists all the cities of California in hbtn_0d_usa
-- Must use a subquery (no JOIN)
-- Results sorted by cities.id ascending

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
