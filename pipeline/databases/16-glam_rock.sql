-- this comment is a description of the script below
SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%_lam rock%'
ORDER BY lifespan DESC LIMIT 100;
