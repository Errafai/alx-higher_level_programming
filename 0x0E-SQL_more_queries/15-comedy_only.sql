-- displays the genres of Dexter tv show
SELECT tv_shows.title
	FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.title ASC;
