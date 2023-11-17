-- Lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
-- Displays `tv_shows.title` and `tv_show_genres.genre_id` ordered by `tv_shows.title` and `tv_show_genres.genre_id.
-- Using one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
