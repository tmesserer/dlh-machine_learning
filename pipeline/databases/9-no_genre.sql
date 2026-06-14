-- this comment is a description of the script below
SELECT a.title, b.genre_id as genre_id
FROM tv_shows a
    LEFT JOIN tv_show_genres b
    ON a.id = b.show_id
WHERE b.show_id IS NULL
ORDER BY a.title, b.genre_id ASC;
