-- Lesson 48
-- 21.01.2024

-- Создать таблицу CREATE TABLE
-- Вариант с прошлого урока хорош, но не всегда удобен
-- Данные о специальности будут дублироваться в каждой строке
-- Менять их будет сложно

--CREATE TABLE students (
--    id    INTEGER PRIMARY KEY AUTOINCREMENT,
--    name  TEXT    NOT NULL,
--    age   INTEGER NOT NULL,
--    major TEXT,
--    gpa   REAL
--);

-- Для удаления старой таблицы используем DROP TABLE
DROP TABLE students;

-- Сделаем табличку с специальностями
-- В ней будет только id и название специальности
CREATE TABLE majors (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    major_name TEXT NOT NULL
);

-- Вставим данные в таблицу majors (множественное добавление записей)
INSERT INTO majors (major_name)
VALUES ('Python web-разработчик'),
       ('Python QA-инженер'),
       ('JavaScript Frontend-разработчик'),
       ('Python Middle-разработчик'),


-- Обновленная таблица students, где вместо major будет major_id - внешний ключ на
-- таблицу majors

CREATE TABLE students (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    age   INTEGER NOT NULL,
    major_id INTEGER,
    gpa   REAL,
    FOREIGN KEY (major_id) REFERENCES majors(id)
);
-- Массово добавим студентов в таблицу students
INSERT INTO students (name, age, major_id, gpa) VALUES
('Анохин Андрей Сергеевич', 20, 1, NULL),
('Гудкова Елена Сергеевна', 20, 1, NULL),
('Козлов Станислав Константинович', 20, 1, NULL),
('Костин Виталий Валерьевич', 20, 1, NULL),
('Кузяев Артур Рамазанович', 20, 1, NULL),
('Кукуяшный Андрей Викторович', 20, 1, NULL),
('Кулагин Владимир Фёдорович', 20, 1, NULL),
('Обухов Максим Олегович', 20, 1, NULL),
('Основин Игорь Александрович', 20, 1, NULL),
('Сахаров Евгений Владимирович', 20, 1, NULL),
('Сидоренко Илья Анатольевич', 20, 1, NULL),
('Соминов Александр Васильевич', 20, 1, NULL),
('Тимофеев Александр Александрович', 20, 1, NULL),
('Хасанов Шердорбек Улугбекович', 20, 1, NULL),
('Шибаев Юрий Николаевич', 20, 1, NULL);

-- Добавим еще одного человека
INSERT INTO students (name, age, major_id, gpa) VALUES
--('Монин Владимир Александрович', 22, 3, 4.5),
('Кузнецов Кузьма Кузьмич', 23, 2, 3.5),
('Анна Ольговна Николаева', 24, 4, 4.5);

-- Получаем данные из одной таблицы студенты
SELECT * FROM students;

-- Получаем все данные из таблицы студентов и название специальности
SELECT students.*, majors.major_name
FROM students
JOIN majors ON students.major_id = majors.id;

-- Такой же запрос с использованием alias (псевдонимов)
select a.*, b.major_name
from students a
join majors b on a.major_id=b.id;

-- Возьмем только имена и названия специальностей
SELECT students.name, majors.major_name
FROM students
JOIN majors ON students.major_id = majors.id;

-- Сделаем группировку по специальностям и посчитаем сколько студентов на каждой специальности
SELECT majors.major_name, COUNT(*) AS "Количество студентов"
FROM students
JOIN majors ON students.major_id = majors.id
GROUP BY majors.major_name;
ORDER BY "Количество студентов" DESC;

-- Сделаем UPDATE - обновим среднюю оценку на 5.0 у всех студентов у которых специальность Python web-разработчик
-- именно по названию специальности
-- Вариант 1
UPDATE students
SET gpa = 5.0
WHERE major_id = (
    SELECT id
    FROM majors
    WHERE major_name = 'Python web-разработчик'
);

-- Вариант 2
UPDATE students
SET gpa = 5.0
WHERE major_id IN (
    SELECT id
    FROM majors
    WHERE major_name = 'Python web-разработчик'
);

-- Удалим студентов с специальностью Python Middle-разработчик
DELETE FROM students
WHERE major_id = (
    SELECT id
    FROM majors
    WHERE major_name = 'Python Middle-разработчик'
);

-- Виды JOIN
-- INNER JOIN - возвращает только те строки, которые есть в обеих таблицах
-- LEFT JOIN - возвращает все строки из левой таблицы и только те строки из правой таблицы, которые есть в левой
-- RIGHT JOIN - возвращает все строки из правой таблицы и только те строки из левой таблицы, которые есть в правой
-- FULL JOIN - возвращает все строки из обеих таблиц

-- Добавляем сутеднта без специальности
INSERT INTO students (name, age, major_id, gpa) VALUES
('Николаева Ольга Павловна', 22, NULL, 4.5);

-- JOIN - INNER JOIN
SELECT students.name, majors.major_name
FROM students
JOIN majors ON students.major_id = majors.id;

-- Получить студентов, даже если у них нет специальности
-- LEFT JOIN
SELECT students.name, majors.major_name
FROM students
LEFT JOIN majors ON students.major_id = majors.id;

-- Получить специальности, даже если у них нет студентов
-- RIGHT JOIN
SELECT students.name, majors.major_name
FROM students
RIGHT JOIN majors ON students.major_id = majors.id;

-- Получить все специальности и всех студентов
-- FULL JOIN
SELECT students.name, majors.major_name
FROM students
FULL JOIN majors ON students.major_id = majors.id;