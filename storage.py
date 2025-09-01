import sqlite3
from datetime import datetime

class StorageHandler:
    """Storage handler for the tracking application."""

    def __init__(self, db_path='db.sqlite3'):
        """Initializes the database connection and creates tables if they don't exist."""
        self.conn = self._connect(db_path)
        self.create_tables()

    def _connect(self, db_path):
        try:
            return sqlite3.connect(db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def create_tables(self):
        """Creates the necessary database tables if they don't exist already.
        
        Creates two tables:
        - habits: Stores habit metadata (id, name, periodicity, creation date)
        - completions: Stores completion records
        """

        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS habits (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        periodicity TEXT NOT NULL,
                        created_at TEXT DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS completions (
                        id INTEGER PRIMARY KEY,
                        habit_id INTEGER NOT NULL,
                        completion_date TEXT DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (habit_id) REFERENCES habits(id)
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise

    def insert_habit(self, name, periodicity):
        """Adds a new habit to the database."""
        try:
            with self.conn:
                cursor = self.conn.execute(
                    "INSERT INTO habits (name, periodicity) VALUES (?, ?)",
                    (name, periodicity)
                )
                return cursor.lastrowid  # Return the ID of the inserted habit
        except sqlite3.Error as e:
            print(f"Error inserting habit: {e}")
            raise

    def fetch_all_habits(self):
        """Retrieves all the habits from the database."""
        try:
            return self.conn.execute("SELECT * FROM habits").fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching habits: {e}")
            raise

    def log_completion(self, habit_id, completion_date= None):
        try:
            cursor = self.conn.execute("SELECT COUNT(*) FROM habits WHERE id=?", (habit_id,))
            if cursor.fetchone()[0] == 0:
                raise ValueError(f"Habit with ID {habit_id} does not exist.")
            if completion_date is None:
                completion_date = datetime.now().isoformat()

            with self.conn:
                self.conn.execute(
                "INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)",
                (habit_id, completion_date)
            )
        except (sqlite3.Error, ValueError) as e:
            print(f"Error logging completion: {e}")
            raise

    def get_completions_for_habit(self, habit_id):
        try:
            return self.conn.execute(
                "SELECT completion_date FROM completions WHERE habit_id = ?",
                (habit_id,)
            ).fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching completions for habit ID {habit_id}: {e}")
            raise

    def delete_habit(self, habit_id):
        """Deletes a habit from the database."""
        try:
            with self.conn:
                self.conn.execute("DELETE FROM completions WHERE habit_id = ?", (habit_id,))
                self.conn.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        except sqlite3.Error as e:
            print(f"Error deleting habit: {e}")
            raise

def delete_completion(self, habit_id, date):
    try:
        with self.conn:
            self.conn.execute(
                "DELETE FROM completions WHERE habit_id = ? AND completion_date LIKE ?",
                (habit_id, f"{date}%")
            )
    except sqlite3.Error as e:
        print(f"Error deleting completion: {e}")
        raise
