-- this comment is a description of the script below
SELECT origin, sum(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC LIMIT 100;
