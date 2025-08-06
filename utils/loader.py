import json
from datetime import datetime

def load_data(rooms_file: str, students_file: str, conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students")
    cursor.execute("DELETE FROM rooms")

    with open(rooms_file, 'r') as f:
        rooms = json.load(f)
        for room in rooms:
            cursor.execute(
                "INSERT INTO rooms (id, name) VALUES (%s, %s)",
                (room['id'], room['name'])
            )

    with open(students_file, 'r') as f:
        students = json.load(f)
        for student in students:
            birthday = datetime.fromisoformat(student['birthday']).date()
            nationality = student.get('nationality', 'Unknown')
            cursor.execute(
                "INSERT INTO students (id, name, birthday, sex, room_id, nationality) VALUES (%s, %s, %s, %s, %s, %s)",
                (student['id'], student['name'], birthday, student['sex'], student['room'], nationality)
            )

    conn.commit()
    cursor.close()
