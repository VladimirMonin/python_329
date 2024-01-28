-- Lesson 49
-- 27.01.2024
-- Сегодня:
-- Транзакции - BEGIN TRANSACTION, COMMIT, ROLLBACK
-- FOREIGN KEY - внешний ключ
-- составной ключ FOREIGN KEY (id1, id2, id3) REFERENCES table(id1, id2, id3)
-- JOIN - объединение таблиц
-- LEFT JOIN - левое объединение
-- RIGHT JOIN - правое объединение
-- FULL JOIN - полное объединение
-- INNER JOIN - внутреннее объединение
-- ON DELETE (CASCADE, SET NULL, SET DEFAULT, RESTRICT)
-- ON UPDATE (CASCADE, SET NULL, SET DEFAULT, RESTRICT)
-- Подзапросы - подзапрос в SELECT, подзапрос в FROM, подзапрос в WHERE
-- Представления - VIEW - виртуальные таблицы
-- Хранимые процедуры - STORED PROCEDURES
-- Триггеры - TRIGGERS

-- SQLite - stu
-- Транзакции - BEGIN TRANSACTION, COMMIT, ROLLBACK
-- Сделаем 1 таблицу со счетами клиентов id, name, balance
-- Добавим 2 клиента с балансами 1000 и 2000 соответственно
-- Сделаем транзакцию которая будет снижать баланс клиента на 1000 и увеличивать баланс другого клиента на 1000
-- При условии что оба клиента существуют и у первого баланс больше 1000

CREATE TABLE clients (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name TEXT(255) NOT NULL,
    balance INT NOT NULL
);

INSERT INTO clients (name, balance) VALUES ('Станислав', 1001);
INSERT INTO clients (name, balance) VALUES ('Евгений', 2000);

BEGIN TRANSACTION;
-- Берем баланс клиента с id = 1 и уменьшаем его на 1000, при условии что баланс больше 1000
UPDATE clients SET balance = balance - 1000
WHERE id = 1 AND balance > 1000;

-- Берем баланс клиента с id = 2 и увеличиваем его на 1000
UPDATE clients SET balance = balance + 1000
WHERE id = 2;

-- Если оба запроса выполнились успешно, то коммитим транзакцию
COMMIT;

-- Если хотя бы один запрос не выполнился, то откатываем транзакцию
ROLLBACK;



-- SQLite диалект
--  - `student_id`: Автоинкрементный первичный ключ. Уникально идентифицирует каждого студента.
--   - `first_name`: Имя студента. Не может быть `NULL` (NOT NULL,TEXT).
--   - `middle_name`: Отчество студента. Может быть пустым. (TEXT).
--   - `last_name`: Фамилия студента. Не может быть `NULL`. (NOT NULL,TEXT).
--   - `group_name`: Название группы, к которой принадлежит студент. Не может быть `NULL`. (NOT NULL,TEXT).
--   - `homework_text`: Готовая домашка от студента (TEXT)
--   - `homework_task`: Текст задания домашней работы. (TEXT)
--   - `homework_id`: Уникальный идентификатор домашней работы. (INTEGER)
--   - `homework_status`: Статус проверки домашней работы (по умолчанию `false`). (text)
--   - `homework_topics`: Темы, связанные с домашней работой. (TEXT)

-- Начинаем транзакцию на диалекте SQLite
BEGIN TRANSACTION;


-- Создаем таблицу студентов
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    homework_text TEXT,
    homework_task TEXT,
    homework_id INTEGER,
    homework_status TEXT DEFAULT 'false',
    homework_topics TEXT
);

-- Массово добавляем студентов
INSERT INTO students (first_name, middle_name, last_name, group_name, homework_text, homework_task, homework_id, homework_status, homework_topics)
VALUES ('Станислав', 'Владимирович', 'Кузнецов', 'БПИ-194', 'Домашка', 'Сделать домашку', 1, 'false', 'SQL'),
('Евгений', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 1, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 2, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 3, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-196', 'Тут моя домашка', 'Сделать домашку', 4, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 5, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 6, 'false', 'SQL'),
('Александр', 'Александрович', 'Кузнецов', 'БПИ-194', 'Тут моя домашка', 'Сделать домашку', 7, 'false', 'SQL');

-- Если все запросы выполнились успешно, то коммитим транзакцию
COMMIT;

-- Удалю первоначальную таблицу
DROP TABLE students;

-- Первая нормальная форма (1NF)
-- 1. Все значения атрибутов должны быть атомарными
-- 2. Все значения атрибутов должны быть однотипными
-- 3. Все значения атрибутов должны быть уникальными

-- Поэтому нам надо сделать отдельные таблицы:
-- 1. Студенты (id, first_name, middle_name, last_name, group_id)
-- 2. Группы (id, group_name)
-- 3. Домашние задания (id, task_text)
-- 4. Домашние задания - темы (homework_id, topic_id)
-- 5. Темы (id, topic_name)
-- 6. Сданные домашние задания (id, work_text, homework_id, student_id, status)
-- 7. Конспекты (id, text)
-- 8. Конспекты - темы (id, topic_id)
-- 9. Выданные домашние задания (homework_id, group_id) - составной внешний ключ

-- Создаем таблицу студентов (Sqlite)
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    group_id INTEGER NOT NULL,

FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Создаем таблицу групп (Sqlite)
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL
);

-- Создаем таблицу домашних заданий (Sqlite)
CREATE TABLE homeworks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_text TEXT NOT NULL
);

-- Создаем таблицу домашних заданий - темы (Sqlite)
CREATE TABLE homeworks_topics (
    homework_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,

FOREIGN KEY (homework_id) REFERENCES homeworks(id),
FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Создаем таблицу тем (Sqlite)
CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_name TEXT NOT NULL
);

-- Создаем таблицу сданных домашних заданий (Sqlite)
CREATE TABLE homeworks_done (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_text TEXT NOT NULL,
    homework_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    status TEXT DEFAULT 'false'

FOREIGN KEY (homework_id) REFERENCES homeworks(id),
FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Создаем таблицу конспектов (Sqlite)
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL
);

-- Создаем таблицу конспектов - темы (Sqlite)
CREATE TABLE notes_topics (
    note_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,

FOREIGN KEY (note_id) REFERENCES notes(id),
FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Добавляем таблицу выданных домашних заданий
CREATE TABLE homeworks_issued (
    homework_id INTEGER NOT NULL,
    group_id INTEGER NOT NULL,

-- Составной внешний ключ
FOREIGN KEY (homework_id, group_id) REFERENCES homeworks(id, group_id)

);

