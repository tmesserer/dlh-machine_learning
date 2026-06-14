-- this comment is a description of the script below
SELECT a.name AS genre, COUNT(c.title) AS number_of_shows
FROM tv_genres a
    INNER JOIN tv_show_genres b
    ON a.id = b.genre_id
        INNER JOIN tv_shows c
        ON b.show_id = c.id 
GROUP BY a.name
ORDER BY COUNT(c.title) DESC;
