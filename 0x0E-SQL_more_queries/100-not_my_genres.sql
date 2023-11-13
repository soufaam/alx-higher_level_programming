-- lists all privileges of the MySQL users user_0d_1 
-- and user_0d_2 on your server (in localhost).
USE hbtn_test_db_shows;
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title IS NULL OR tv_shows.title != 'Dexter'
ORDER BY tv_genres.name ASC;