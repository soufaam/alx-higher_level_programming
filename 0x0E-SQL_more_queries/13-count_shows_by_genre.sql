-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows FROM tv_genres 
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows
 DESC;
