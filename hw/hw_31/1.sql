SELECT id, name, city, address, category, subcategory
FROM [2gis_businesses]
WHERE city = "Балашиха" AND category IN ("Продажа билеов", "Авиатранспорт")
ORDER BY subcategory, name DESC