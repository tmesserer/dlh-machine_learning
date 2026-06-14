-- this comment is a description of the script below
SELECT a.title, SUM(b.rate) AS rating_sum
FROM tv_shows a
    INNER JOIN tv_show_ratings b
    ON a.id = b.show_id
GROUP BY a.title
ORDER BY SUM(b.rate) DESC;
