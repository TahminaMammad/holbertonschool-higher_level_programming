-- 14-my_genres.sql
-- Script that lists all genres of the show Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- Only one SELECT statement

SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id
  AND tv_shows.id = tv_show_genres.show_id
  AND tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
