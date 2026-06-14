-- this comment is a description of the script below
SELECT a.title, c.id AS genre_id
FROM tv_shows a
    INNER JOIN tv_show_genres b
    ON a.id = b.show_id
        INNER JOIN tv_genres c
        ON b.genre_id = c.id 
ORDER BY a.title, c.id ASC;
