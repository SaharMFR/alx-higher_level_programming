-- Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
-- Display `tv_shows.title` and `tv_show_genres.genre_id`.
-- Ordered by `tv_shows.title` and `tv_show_genres.genre_id`.
-- Using one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
