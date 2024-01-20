-- Задача №5
--"Запрягай телегу!" Ищем уникальные записи Телеграм где телеграмм есть
-- 71671
SELECT DISTINCT telegram, name
FROM "2gis_businesses"
WHERE telegram not null
ORDER BY telegram
