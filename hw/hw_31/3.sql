-- Задача №3
-- "Ищу котики но не наркотики!". Все что содержит похожее на "котик" но не похожее на "наркотик" в названии в Москве
-- 3 строки
SELECT name, city
FROM "2gis_businesses"
WHERE city = 'Москва'
AND name LIKE "%котик%"
AND name NOT LIKE "%наркотик%"
ORDER BY city, name;