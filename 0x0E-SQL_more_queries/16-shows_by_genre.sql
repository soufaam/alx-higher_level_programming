-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).

SELECT tv_shows.title, tv_genres.name  AS name FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id 
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
 ORDER BY tv_shows.title,  tv_genres.name ASC
;
