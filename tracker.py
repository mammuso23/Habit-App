from storage import StorageHandler
from habit import Habit
from datetime import datetime

class HabitTracker:
    def __init__(self, db_path="db.sqlite3"):
        self.storage = StorageHandler(db_path)
        self.habits = self.load_habits()

    def load_habits(self):
        raw_habits = self.storage.fetch_all_habits()
        return [
            Habit(habit_id=row[0], name=row[1], periodicity=row[2], created_at=row[3]) 
            for row in raw_habits
        ]

    def add_habit(self, name, periodicity):
        habit_id = self.storage.insert_habit(name, periodicity)
        self.habits.append(Habit(habit_id=habit_id, name=name, periodicity=periodicity))

    def mark_complete(self, habit_id, date = None):
         if date is None:
             date = datetime.now().isoformat()
         self.storage.log_completion(habit_id, date)

    def get_completion_lookup(self):
        return {
            habit.habit_id: [c[0][:10] for c in self.storage.get_completions_for_habit(habit.habit_id)]
            for habit in self.habits
        }
        return lookup
    
    def delete_habit(self, habit_id):
        self.storage.delete_habit(habit_id)
        self.habits = [h for h in self.habits if h.habit_id != habit_id]

    def undo_completion(self, habit_id, date):
        self.storage.delete_completion(habit_id, date)
