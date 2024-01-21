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

-- Получаем данные из одной таблицы студенты
SELECT * FROM students;

