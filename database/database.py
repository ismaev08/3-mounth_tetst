import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS homeworks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            python_group TEXT,
            homework_number INTEGER,
            git_url TEXT
            )
            """)
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()