-- List Cities that can be found in database
SELECT states.id, cities.name
FROM states join cities on
(states.id = cities.state_id)
ORDER BY cities.id ASC;
