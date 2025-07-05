import psycopg2
from faker import Faker
import os
import time

fake = Faker()

def connect():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            return conn
        except:
            retries -= 1
            time.sleep(2)
    raise Exception("Could not connect to DB")

def init_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE
        );
    """)
    conn.commit()

    # Seed fake users
    cur.execute("SELECT COUNT(*) FROM users;")
    count = cur.fetchone()[0]
    if count == 0:
        for _ in range(10):
            name = fake.name()
            email = fake.email()
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    init_db()
