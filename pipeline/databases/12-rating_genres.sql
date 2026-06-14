-- this comment is a description of the script below
SELECT c.name, SUM(a.rate) AS rating
FROM tv_show_ratings a
    INNER JOIN tv_show_genres b
    ON a.show_id = b.show_id
        INNER JOIN tv_genres c
        ON b.genre_id = c.id
GROUP BY c.name
ORDER BY SUM(a.rate) DESC;