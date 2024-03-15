--Import the database dump of hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows RIGHT JOIN tv_show_genres
--    -LEFT-        -RIGHT-    --
ON
    tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;