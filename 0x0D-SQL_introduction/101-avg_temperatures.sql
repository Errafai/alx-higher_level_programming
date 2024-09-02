-- displays the avrage tempeture by city and order by temptrue
SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
