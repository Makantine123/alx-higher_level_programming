-- List Cities that can be found in database
SELECT c.id, c.name FROM cities AS c, states AS s
       WHERE c.state_id=s.id AND s.name = "California"
       ORDER BY c.id ASC;
