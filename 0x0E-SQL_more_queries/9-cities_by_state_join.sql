-- List all cities contained in the database
SELECT c.id, c.name, s.name FROM cities c,
	INNNER JOIN states s ON c.state_id = s.id
	ORDER BY c.id ASC;

