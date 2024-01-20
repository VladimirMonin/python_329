-- Задача №6
--"А поговорить?." Ищем все записи где номер начинается на 8-800 (тире может быть разным)
-- 73675 записей
SELECT name, phone
FROM "2gis_businesses"
WHERE phone not null AND phone LIKE "%8%800%"