-- List all cities contained in the database
SELECT c.id, c.name, s.name FROM cities as c, states as s
WHERE c.state_id = s.id
ORDER BY c.id ASC
