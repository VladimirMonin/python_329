-- Возможно ли добыть запись после удаления?
-- Обязательна ли переиндексация базы данных?


-- CRUD - Create, Read, Update, Delete
-- Создать, прочитать, обновить, удалить
-- INSERT INTO - Вставить данные

-- Создать таблицу CREATE TABLE
CREATE TABLE students (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    age   INTEGER NOT NULL,
    major TEXT,
    gpa   REAL
);

-- Вставить данные INSERT INTO
-- добавляем записи об одном студенте с перечнем всех полей
INSERT INTO students (name, age, major, gpa)
VALUES ('Иванов Иван Иванович', 20, 'История', 4.5);

-- Добавляем не полную запись (студент без GPA)
INSERT INTO students (name, age, major)
VALUES ('Петров Петр Петрович', 21, 'Физика');

-- Добавялем несколько записей за один раз
INSERT INTO students (name, age, major, gpa)
VALUES ('Сидоров Сидор Сидорович', 22, 'Математика', 4.0),
       ('Кузнецов Кузьма Кузьмич', 23, 'Физика', 3.5),
       ('Анна Ольговна Николаева', 24, 'История', 4.5);
--
select * from students

-- Удалить данные где id = 1
DELETE FROM students
WHERE id = 6;

-- Обновим запись с id 3 (изменим имя) Иванов Иван Ивановыч
UPDATE students
SET name = 'Иванов Иван Ивановыч'
WHERE id = 3;

-- Обновим возраст всех студентов на +1 год
UPDATE students
SET age = age + 1;

-- Обновим физику на Ядерная физика
UPDATE students
SET major = 'Ядерная физика'
WHERE major = 'Физика';

-- Обновим ВСЕ студенту с id 7
UPDATE students
SET name = 'Хельга Браун',
    age = "двадцать пять",
    major = 'История',
    gpa = 4.5
WHERE id = 7;

-- Таблица для практики

CREATE TABLE [2gis_businesses] (
    id              INTEGER NOT NULL,
    gis_id          INTEGER,
    name            VARCHAR NOT NULL,
    region          VARCHAR,
    district        VARCHAR,
    city            VARCHAR,
    city_district   VARCHAR,
    address         VARCHAR,
    [index]         VARCHAR,
    phone           VARCHAR,
    mobile_phone    VARCHAR,
    email           VARCHAR,
    website         VARCHAR,
    category        VARCHAR,
    subcategory     VARCHAR,
    working_hours   VARCHAR,
    payment_methods VARCHAR,
    whatsapp        VARCHAR,
    viber           VARCHAR,
    telegram        VARCHAR,
    facebook        VARCHAR,
    instagram       VARCHAR,
    vkontakte       VARCHAR,
    odnoklassniki   VARCHAR,
    youtube         VARCHAR,
    twitter         VARCHAR,
    skype           VARCHAR,
    icq             VARCHAR,
    googleplus      VARCHAR,
    linkedin        VARCHAR,
    pinterest       VARCHAR,
    latitude        FLOAT,
    longitude       FLOAT,
    PRIMARY KEY (
        id
    )
);

-- 0.325 секунды
SELECT name, city
FROM "2gis_businesses"
WHERE city = 'Москва'
AND name LIKE "%котик%"
AND name NOT LIKE "%наркотик%"
ORDER BY city, name;

-- Создаем индекс для ускорения поиска LIKE по name
CREATE INDEX idx_name ON [2gis_businesses] (name);

-- После индекса +500% скорость 0.064 секунды