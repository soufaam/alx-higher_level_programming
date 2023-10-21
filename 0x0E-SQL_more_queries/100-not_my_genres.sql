-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).

SELECT  tv_genres.name  AS name FROM tv_genres 
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id 
INNER JOIN tv_shows ON tv_show_genres.genre_id = tv_shows.id 
AND tv_shows.title = 'Dexter' ORDER BY tv_genres.name ;
