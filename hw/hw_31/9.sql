-- Задача №9
-- "Письмо в Подмосковье" Где есть индекс и он между 141001 AND 141720
-- 73558 строк
SELECT DISTINCT [index], city, name, address
FROM "2gis_businesses"
WHERE [index] not null and [index] BETWEEN 141001 AND 141720
ORDER BY [index]