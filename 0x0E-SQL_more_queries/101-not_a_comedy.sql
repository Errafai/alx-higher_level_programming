-- displays all the tv shows that don't have a commed genre
SELECT DISTINCT title
	FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = 5
	LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id AND tv_genres.name = "Comedy"
	WHERE tv_genres.id IS NULL
	ORDER BY title ASC;
