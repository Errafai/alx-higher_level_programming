-- list the name and score of second table
SELECT score, name FROM second_table
	WHERE score IS NOT NULL AND name NOT NULL
	ORDER BY score desc;
