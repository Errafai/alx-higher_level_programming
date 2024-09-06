-- list all tv shows with thier genresa
SELECT tv_genres.name as genre, number.number_of_shows
	FROM tv_genres INNER JOIN (
		SELECT genre_id, COUNT(show_id) AS number_of_shows
		FROM tv_show_genres
		GROUP BY genre_id
	) AS number
	ON number.genre_id = tv_genres.id
	ORDER BY number_of_shows DESC;
