-- list city name and id
-- list state name
SELECT c.id, c.name, s.name
FROM cities c
INNER JOIN states s
ON c.state_id = s.id
ORDER BY c.id ASC;
