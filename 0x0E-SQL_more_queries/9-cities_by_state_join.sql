-- List all cities contained in the database
SELECT c.id, c.name, s.name
FROM cities as c,
INNNER JOIN states as s
ON c.state_id = s.id
ORDER BY c.id ASC;
