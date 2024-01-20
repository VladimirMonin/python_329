-- Задача №7
--"Передаю координаты." Ищем все записи в latitude между 55.75 AND 55.80 и longitude между 37.60 AND 37.65
-- 25060 записей
SELECT name, address FROM "2gis_businesses"
WHERE (latitude
BETWEEN 55.75 AND 55.80)
AND (longitude BETWEEN 37.60 AND 37.65);