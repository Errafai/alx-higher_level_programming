-- show scores and number of repeted scores
SELECT score, COUNT(score) AS number
	GROUP BY score
	ORDER BY number desc;
