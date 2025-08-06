import argparse
from utils.loader import load_data
from utils.exporter import export_results
from queries import (
    get_room_student_count,
    get_lowest_avg_age_rooms,
    get_highest_age_diff_rooms,
    get_multinational_rooms
)
from database import get_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Student Room Database CLI")
    parser.add_argument("--students", required=True, help="Path to students JSON file")
    parser.add_argument("--rooms", required=True, help="Path to rooms JSON file")
    parser.add_argument("--format", required=True, choices=["json", "xml"], help="Output format")
    args = parser.parse_args()

    conn = get_connection()
    logger.info("Loading data into the database...")
    load_data(args.rooms, args.students, conn)

    logger.info("Executing queries...")
    results = {
        "room_student_count": get_room_student_count(conn),
        "lowest_avg_age_rooms": get_lowest_avg_age_rooms(conn),
        "highest_age_diff_rooms": get_highest_age_diff_rooms(conn),
        "multinational_rooms": get_multinational_rooms(conn)
    }

    logger.info(f"Exporting results to output.{args.format} ...")
    export_results(results, args.format, f"output.{args.format}")

    conn.close()

if __name__ == "__main__":
    main()
