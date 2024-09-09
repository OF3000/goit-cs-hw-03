from faker import Faker
import psycopg2
import random

fake = Faker()

db_config = {
    "dbname": "HW3",
    "user": "postgres",
    "password": "0947",
    "host": "localhost",
}


def generate_users(n=10):
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users


def generate_statuses():
    statuses = [("new",), ("in progress",), ("completed",)]
    return statuses


def generate_tasks(n=30):
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 3)
        user_id = random.randint(1, 10)
        tasks.append((title, description, status_id, user_id))
    return tasks


def populate_db():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        users = generate_users()
        cur.executemany("Insert into users (fullname, email) VALUES (%s, %s)", users)

        statuses = generate_statuses()
        cur.executemany("Insert into status (name) VALUES (%s)", statuses)

        tasks = generate_tasks()
        cur.executemany(
            "Insert into tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            tasks,
        )

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    populate_db()
