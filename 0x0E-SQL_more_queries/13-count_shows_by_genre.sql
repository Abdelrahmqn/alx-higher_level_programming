-- select all genres by counting them
SELECT tv_genres.name AS genre FROM tv_shows AS shows
WHERE id = (
    WHERE id FROM shows
    genre = 'Dexter'
)
ORDER BY genre ASC;