-- Задача №1
-- "Пишу в Москву". Все что содержит похожее на "кафе" или "магазин" в категории с емейлами в Москве
-- 11264 строки в ответе
SELECT name, city, address
FROM "2gis_businesses"
WHERE (city = 'Москва')
AND (category LIKE 'кафе%' OR category LIKE '%магазин%')
AND email IS NOT NULL
ORDER BY city, name;