-- list all tv shows with thier genres
SELECT tv_shows.title, tv_show_genres.genre_id
	from tv_shows inner join tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
