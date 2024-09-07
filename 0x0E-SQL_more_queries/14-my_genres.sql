-- displays the genres of Dexter tv show
SELECT DISTINCT name, genre_id
	FROM tv_genres, tv_show_genres
	WHERE (SELECT id FROM tv_shows WHERE title = "Dexter") = tv_show_genres.show_id AND tv_show_genres.genre_id = tv_genres.id
	ORDER BY name ASC;
