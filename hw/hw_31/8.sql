-- Задача №8
-- "За наличку." - Ищем все фирмы где есть оплата наличкой
-- 504232 записей
SELECT name, payment_methods FROM "2gis_businesses"
WHERE payment_methods LIKE '%Налич%'