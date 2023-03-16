-- Number of records with same score
SELECT score, COUNT(number) as number FROM second_table GROUP BY score ORDER BY score DESC
