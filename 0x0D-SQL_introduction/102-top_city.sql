-- displays the top 3 of cities temparatures during july and August
SELECT city, AVG(value) AS avg_temp
        FROM temperatures
		WHERE month = 7 Or month = 8
        GROUP BY city
        ORDER BY avg_temp DESC
		LIMIT 3;
