-- Задача №2
-- "Ищу котоиков!". Все что содержит похожее на "котик" в названии в Москве
-- 10 cтрок в ответе
SELECT name, city, address
FROM "2gis_businesses"
WHERE (city = 'Москва')
AND (name LIKE "%котик%")
ORDER BY city, name;