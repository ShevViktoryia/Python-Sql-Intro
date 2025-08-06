CREATE TABLE IF NOT EXISTS rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    sex CHAR(1) NOT NULL,
    room_id INT REFERENCES rooms(id),
    nationality VARCHAR(255)
);

CREATE INDEX IF NOT EXISTS idx_students_room_id ON students(room_id);
CREATE INDEX IF NOT EXISTS idx_students_birthday ON students(birthday);
CREATE INDEX IF NOT EXISTS idx_students_nationality ON students(nationality);
