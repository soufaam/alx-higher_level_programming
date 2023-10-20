-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).

SELECT tv_genres.name AS name FROM tv_shows 
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name
;
