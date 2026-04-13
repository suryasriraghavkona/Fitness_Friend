import sqlite3
from datetime import datetime

conn = sqlite3.connect("fitness.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS fitness (
    date TEXT,
    activity TEXT,
    value REAL
)
""")
conn.commit()

def insert_data(activity, value):
    c.execute("INSERT INTO fitness VALUES (?, ?, ?)",
              (str(datetime.now().date()), activity, value))
    conn.commit()

def fetch_data():
    c.execute("SELECT * FROM fitness")
    return c.fetchall()