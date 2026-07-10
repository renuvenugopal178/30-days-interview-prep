-- Day 6: SQL and DBMS Practice
-- Reset database first, so this file can be run again safely.

DROP TABLE IF EXISTS registrations;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

-- Test connection
SELECT 'SQLite is running' AS message;

-- 1. CREATE TABLES

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT
);

CREATE TABLE events (
    event_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT,
    organizer_id INTEGER,
    FOREIGN KEY (organizer_id) REFERENCES users(user_id)
);

CREATE TABLE registrations (
    registration_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    event_id INTEGER,
    registration_date TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- 2. INSERT DATA

INSERT INTO users (user_id, name, email, city)
VALUES
    (1, 'Renu', 'renu@example.com', 'Kottayam'),
    (2, 'Anu', 'anu@example.com', 'Kozhikode'),
    (3, 'Arun', 'arun@example.com', 'Kochi'),
    (4, 'Meera', 'meera@example.com', 'Kottayam');

INSERT INTO events (event_id, title, event_date, location, organizer_id)
VALUES
    (101, 'AI Workshop', '2026-08-10', 'Kozhikode', 1),
    (102, 'Cybersecurity Meetup', '2026-09-01', 'Kochi', 2),
    (103, 'React Bootcamp', '2026-09-15', 'Online', 1),
    (104, 'Python Basics', '2026-10-01', 'Kottayam', 3);

INSERT INTO registrations (
    registration_id,
    user_id,
    event_id,
    registration_date,
    status
)
VALUES
    (1001, 2, 101, '2026-07-10', 'confirmed'),
    (1002, 3, 101, '2026-07-10', 'confirmed'),
    (1003, 1, 102, '2026-07-12', 'pending'),
    (1004, 4, 103, '2026-07-15', 'confirmed');

-- 3. VERIFY DATA

SELECT * FROM users;
SELECT * FROM events;
SELECT * FROM registrations;