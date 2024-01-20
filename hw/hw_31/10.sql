-- Задача №10
-- "Пьём на Арбате" Где в названии есть Красное& и в адресе Арбат
-- 1 строка
SELECT name, address
FROM "2gis_businesses"
WHERE name LIKE "%Красное%&%" AND address LIKE "%Арбат%"