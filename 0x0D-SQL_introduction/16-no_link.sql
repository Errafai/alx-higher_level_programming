-- list the name and score of second table
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score desc;
