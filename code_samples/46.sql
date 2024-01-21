-- 14.01.2024 Lesson 46
-- Сегодня проходим:
-- ORDER BY
-- HAVING
-- LIKE
-- Агрегатные функции

-- GROUP BY - группировка по столбцу
-- В данном случае мы группируем по столбцу city (получим уникальные значения)
-- В целом нам это ничего не даст, но чуть позже к каждой позиции можно будет применить функцию

SELECT city
FROM "2gis_businesses"
GROUP BY city

-- COUNT - подсчет количества строк из выборки (ВСЁ)
SELECT COUNT(*) AS "Всего записей"
FROM "2gis_businesses";

-- COUNT(DISTINCT) - подсчет количества уникальных строк из выборки
SELECT COUNT(DISTINCT city) AS "Всего записей"
FROM "2gis_businesses"
--WHERE city IS NOT NULL


-- Группировка по району, где район не NULL (получаем строк сколько всего уникальных районов)
SELECT city, city_district
FROM "2gis_businesses"
WHERE city_district NOT NULL
GROUP BY city_district
ORDER BY city_district DESC


-- Добавляем функцию к предыдущему запросу и получаем количество бизнесов в каждом районе
SELECT city, city_district, COUNT(*) AS "Количество бизнесов в районе"
FROM "2gis_businesses"
WHERE city_district NOT NULL
GROUP BY city_district
ORDER BY city_district DESC

-- TODO Посчитайте количество бизнесов в каждом городе
SELECT city, COUNT(*) AS "Количество бизнесов в городе"
FROM "2gis_businesses"
GROUP BY city
ORDER BY "Количество бизнесов в городе" DESC

-- Фильтрация ДО группировки - WHERE
-- Фильтрация ПОСЛЕ группировки - HAVING
-- Этот же запрос, но только те города в выдаче, где бизнесов больше 5000
SELECT city, COUNT(*) AS Бизнесы
FROM "2gis_businesses"
GROUP BY city
HAVING Бизнесы > 5000
ORDER BY "Количество бизнесов в городе" DESC

-- Ищем всё Красное и белое :)
SELECT city, name, category, subcategory
FROM "2gis_businesses"
WHERE name LIKE "%Красное%&%"

-- Считаем количество Красного и белого по городам
SELECT city, COUNT(*) AS "Количество Красного и белого"
FROM "2gis_businesses"
WHERE name LIKE "%Красное%&%"
GROUP BY city
ORDER BY "Количество Красного и белого" DESC

-- Такой же запрос на Бристоль, но только с категорией напитки (там много лишнего)
SELECT city, COUNT(*) AS "Количество магазинов Бристоль"
FROM "2gis_businesses"
WHERE name LIKE "%Бристоль"
GROUP BY city
ORDER BY "Количество магазинов Бристоль" DESC

-- Поискали Бристоль по по разным категориям. Чтобы понять, что исключить из выборки
-- Обнаружено: ("Автосервис", "Жилищно-коммунальные услуги",
-- "Общественное питание", "Новостройки")
SELECT category, COUNT(*)
FROM "2gis_businesses"
WHERE name LIKE "%Бристоль%"
GROUP BY category
ORDER BY COUNT(*) DESC

-- Теперь мы можем сделать запрос как для "Красное и белое"
-- Только с исключением категорий
SELECT city, COUNT(*) AS "Количество магазинов Бристоль"
FROM "2gis_businesses"
WHERE name LIKE "%Бристоль"
AND category NOT IN ("Автосервис", "Жилищно-коммунальные услуги", "Общественное питание", "Новостройки")
GROUP BY city
ORDER BY "Количество магазинов Бристоль" DESC

-- Попробуем сделать эти два запроса (Красное и белое и Бристоль) в одном запросе
-- Неработает! (Нужны подзапросы)
SELECT city, COUNT(*) AS "Количество магазинов Бристоль",
COUNT(*) AS "Количество Красное и белое"
FROM "2gis_businesses"
WHERE (name LIKE "%Бристоль" --OR name LIKE "%Красное%&%"
AND category NOT IN ("Автосервис", "Жилищно-коммунальные услуги",
"Общественное питание", "Новостройки"))
OR name LIKE "%Красное%&%"
GROUP BY city

-- Запрос от Елены
select city, "количество магазинов Бристоль",
"количество магазинов Красное"

from (
select city,count(*) as "количество магазинов Бристоль"
from "2gis_businesses"
where name like "%Бристоль%"
and category like "%Напитки%"
group by city
order by "количество магазинов Бристоль" desc)
a
left join
(select city,count(*) as "количество магазинов Красное"
from "2gis_businesses"
where
name like "%Красное%&%"
group by city
order by "количество магазинов Красное" desc)
b on b.city=a.city