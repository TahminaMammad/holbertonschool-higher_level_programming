-- 13-count_shows_by_genre.sql
-- Script that lists all genres and the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don't display genres with no shows linked
-- Results must be sorted in descending order by number_of_shows
-- Only one SELECT statement

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
