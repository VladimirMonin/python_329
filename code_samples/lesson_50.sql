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
-- Создаем таблицу студентов если её нет
--CREATE TABLE IF NOT EXISTS students (
-- Если таблица уже есть, удаляем и создаем новую
--DROP TABLE IF EXISTS students;
--CREATE TABLE students (
CREATE TABLE IF NOT EXISTS students (
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
    status TEXT DEFAULT 'false',

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
-- Возьмем и добавим это руками в пайтон в виде строки:
-- Добавляем группу в таблицу групп
INSERT INTO groups (group_name) VALUES ('python329');

-- Добавляем студентов в таблицу студентов (id group= 1)
INSERT INTO students (first_name, middle_name, last_name, group_id) VALUES
('Андрей', 'Сергеевич', 'Анохин', 1),
('Елена', 'Сергеевна', 'Гудкова', 1),
('Станислав', 'Константинович', 'Козлов', 1),
('Виталий', 'Валерьевич', 'Костин', 1),
('Артур', 'Рамазанович', 'Кузяев', 1),
('Андрей', 'Викторович', 'Кукуяшный', 1),
('Владимир', 'Фёдорович', 'Кулагин', 1),
('Максим', 'Олегович', 'Обухов', 1),
('Игорь', 'Александрович', 'Основин', 1),
('Евгений', 'Владимирович', 'Сахаров', 1),
('Илья', 'Анатольевич', 'Сидоренко', 1),
('Александр', 'Васильевич', 'Соминов', 1),
('Александр', 'Александрович', 'Тимофеев', 1),
('Шердорбек', 'Улугбекович', 'Хасанов', 1),
('Юрий', 'Николаевич', 'Шибаев', 1);


-- Добываем данные из таблицы групп
SELECT * FROM groups;

-- Добываем данные из таблицы студентов, подставляя вместо id группы её название
SELECT students.id, students.first_name, students.middle_name, students.last_name, groups.group_name FROM students
JOIN groups ON students.group_id = groups.id;
