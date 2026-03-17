import sqlite3

conn = sqlite3.connect("blood.db", check_same_thread=False)
cursor = conn.cursor()

# Hospitals table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

# Blood inventory
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    hospital TEXT,
    blood_group TEXT,
    component TEXT,
    units INTEGER
)
""")

# Donors
cursor.execute("""
CREATE TABLE IF NOT EXISTS donors (
    name TEXT,
    blood_group TEXT,
    phone TEXT,
    city TEXT
)
""")

conn.commit()