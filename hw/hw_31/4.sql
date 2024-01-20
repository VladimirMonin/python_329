-- Задача №4
-- "Ищу досуг на Тверской". Все что содержит в названии похожее на "Тверская" и в категории похожее на "досуг"
-- 30 строк
SELECT name, city, category, subcategory, address
FROM "2gis_businesses"
WHERE address LIKE '%Тверская%'
AND category LIKE '%досуг%'
ORDER BY category, subcategory