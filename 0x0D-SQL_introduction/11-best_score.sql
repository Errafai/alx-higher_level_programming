-- show all scores >= 10 in the second_table
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score desc;
