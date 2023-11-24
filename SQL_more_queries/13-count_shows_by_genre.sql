-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT genre, COUNT(tv_show_id) AS number_of_shows
FROM hbtn_0d_tvshows
JOIN hbtn_0d_tvshows_genres ON hbtn_0d_tvshows.id = hbtn_0d_tvshows_genres.tv_show_id
JOIN hbtn_0d_genres ON hbtn_0d_tvshows_genres.genre_id = hbtn_0d_genres.id
GROUP BY genre
HAVING COUNT(tv_show_id) > 0
ORDER BY number_of_shows DESC;
