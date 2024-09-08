-- show all genres that are not related to 'Dexter' tv show
 SELECT name
	FROM tv_genres LEFT JOIN (
		SELECT title, genre_id
		FROM tv_shows INNER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
		WHERE title = 'Dexter'
	) AS shows
	ON tv_genres.id = shows.genre_id
	WHERE shows.genre_id IS NULL
	ORDER BY name ASC;
