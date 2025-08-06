def get_room_student_count(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT r.name AS room, COUNT(s.id) AS student_count
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            ORDER BY student_count DESC
        """)
        cols = [desc[0] for desc in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

def get_lowest_avg_age_rooms(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT r.name AS room, AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, s.birthday))) AS avg_age
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            ORDER BY avg_age ASC
            LIMIT 5
        """)
        cols = [desc[0] for desc in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

def get_highest_age_diff_rooms(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT r.name AS room,
                   (MAX(s.birthday) - MIN(s.birthday)) AS age_diff_days
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            ORDER BY age_diff_days DESC
            LIMIT 5
        """)
        cols = [desc[0] for desc in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

def get_multinational_rooms(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT r.name AS room
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id
            HAVING COUNT(DISTINCT s.nationality) > 1
        """)
        cols = [desc[0] for desc in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]
