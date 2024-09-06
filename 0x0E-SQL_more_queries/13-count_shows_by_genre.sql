-- list all tv shows with thier genresa
SELECT tv_genres.name, number.number_of_shows
	FROM tv_genres INNER JOIN (
		SELECT genre_id, COUNT(show_id)
		AS number_of_shows
		FROM tv_show_genres
		GROUP BY genre_id
	) AS number
	WHERE number.genre_id = tv_genres.id
	ORDER BY number_of_shows DESC;
