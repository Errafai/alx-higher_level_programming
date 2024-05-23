-- show scores and number of repeted scores
SELECT score, COUNT(score) AS number
	FROM second_table
	GROUP BY score
	ORDER BY number desc;
