-- 15-comedy_only.sql
-- Script that lists all Comedy shows in hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- Only one SELECT statement

SELECT tv_shows.title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
  AND tv_genres.id = tv_show_genres.genre_id
  AND tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
