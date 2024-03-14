--Import the database dump from hbtn_0d_tvshows
tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC,
tv_show_genres.genre_id ASC;