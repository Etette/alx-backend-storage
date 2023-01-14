-- script that lists all bands with glam rock as their main style, ranked by their longetivity

SELECT
	band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style Like '%Glam rock%';
