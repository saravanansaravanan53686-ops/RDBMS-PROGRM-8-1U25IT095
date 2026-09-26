import mysql.connector
import re
import sys

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "EmployeeDB"
}


def connect_db():
    return mysql.connector.connect(**DB_CONFIG)


def read_solution():
    try:
        with open("solution.sql", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("ERROR: solution.sql file not found.")
        sys.exit(1)


def test_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = 'EmployeeDB'
        AND table_name = 'Employee'
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert result == 1, "Employee table does not exist."
    print("PASS: Employee table exists.")


def test_records():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Employee")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert count == 5, f"Expected 5 records, but found {count}."
    print("PASS: Employee table contains 5 records.")


def test_count():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(Salary) FROM Employee")
    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert result == 5, f"COUNT() expected 5, got {result}."
    print("PASS: COUNT(Salary) = 5")


def test_max():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(Salary) FROM Employee")
    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert float(result) == 45000, f"MAX() expected 45000, got {result}."
    print("PASS: MAX(Salary) = 45000")


def test_min():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT MIN(Salary) FROM Employee")
    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert float(result) == 25000, f"MIN() expected 25000, got {result}."
    print("PASS: MIN(Salary) = 25000")


def test_avg():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(Salary) FROM Employee")
    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert float(result) == 35000, f"AVG() expected 35000, got {result}."
    print("PASS: AVG(Salary) = 35000")


if __name__ == "__main__":
    solution = read_solution()

    required_functions = ["COUNT", "MAX", "MIN", "AVG"]

    for function in required_functions:
        assert re.search(r"\b" + function + r"\s*\(", solution, re.IGNORECASE), \
            f"{function}() function is missing from solution.sql"

    print("PASS: COUNT(), MAX(), MIN(), and AVG() functions found.")

    test_table()
    test_records()
    test_count()
    test_max()
    test_min()
    test_avg()

    print("\nALL TESTS PASSED!")
