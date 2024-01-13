--Lesson 45
--13-01-2024

--выбрать все из 2gis_businesses
SELECT * FROM "2gis_businesses"

--выбрать столбцы name, city, website из 2gis_businesses + все строки
SELECT name, city, website FROM "2gis_businesses"

-- выбрать столбцы name, city, website из 2gis_businesses все строки где name = "Бристоль"
SELECT name, city, website
FROM "2gis_businesses"
WHERE name == "Бристоль"

-- выбрать столбцы name, city, website из 2gis_businesses все строки где name = "Бристоль" или "Бристоль-Парк"
SELECT city, website
FROM "2gis_businesses"
WHERE name == "Красное & Белое" OR name == "Бристоль"

-- выбрать все из "2gis_businesses" где name = Гостиницы и нет website
SELECT *
FROM "2gis_businesses"
WHERE subcategory == "Гостиницы" AND website IS NULL


-- выбрать все из "2gis_businesses" где name входит в перечень и нет website или telegram
-- скобки важны. Иначе AND работает раньше чем OR и выдает ВСЕ записи где есть сайт
SELECT *
FROM "2gis_businesses"
WHERE subcategory IN ("Гостиницы", "Автомойки", "Автошколы")
AND (website IS NULL OR telegram IS NULL)

-- DISTINCT - уникальные значения
-- выбрать все уникальные значения из столбца subcategory и отсортировать в обратном порядке
SELECT DISTINCT subcategory AS "Подкатегория"
FROM "2gis_businesses"
ORDER by subcategory DESC

-- LIKE - поиск по шаблону
-- % - любое количество символов (ДО или ПОСЛЕ)
SELECT DISTINCT category AS "Категория", subcategory AS "Подкатегория"
FROM "2gis_businesses"
WHERE category LIKE "%Химия%" AND category LIKE "%Автосервис%"
ORDER by category


SELECT DISTINCT name AS "Название", category AS "Категория", subcategory AS "Подкатегория"
FROM "2gis_businesses"
WHERE category LIKE "%Химия%" AND subcategory LIKE "%сырьё%"
ORDER by name

-- LIMIT - ограничение количества строк
-- OFFSET - смещение (пропуск) строк
SELECT DISTINCT category AS "Категория"
FROM "2gis_businesses"
WHERE category LIKE "%Химия%"
ORDER by category DESC
LIMIT 10 OFFSET 10

-- COUNT - подсчет количества строк
SELECT COUNT(*) FROM "2gis_businesses";

-- COUNT - подсчет количества строк ГДЕ category LIKE "Химия%"
SELECT COUNT(*)
FROM "2gis_businesses"
WHERE category LIKE "Химия%"

-- COUNT - подсчет количества строк ГДЕ УНИКАЛЬНЫЙ city
SELECT COUNT(DISTINCT city)
FROM "2gis_businesses";

-- GROUP BY - группировка по столбцу (собирает все строки с одинаковым значением в одну)
-- COUNT(*) - подсчет количества строк в группе * - все строки
SELECT city, COUNT(*) as buisness_count
FROM "2gis_businesses"
GROUP BY city
ORDER BY buisness_count DESC

-- Пример от Елены :)
select * from (
select city, count(*) as buisness_count
from "2gis_businesses"
group by city
order by buisness_count desc)
where buisness_count>=100