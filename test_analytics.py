import unittest
from tracker import HabitTracker
from analytics import calculate_longest_streak
from test_data import predefined_habits
from datetime import datetime

class TestHabitAnalytics(unittest.TestCase):

    def setUp(self):
        self.tracker = HabitTracker(":memory:")
        for habit in predefined_habits:
            self.tracker.add_habit(habit["name"], habit["periodicity"])
            habit_id = self.tracker.habits[-1].habit_id
            for date_str in habit["completion_dates"]:
                self.tracker.mark_complete(habit_id, date=date_str)

    def test_streaks(self):
        for habit in predefined_habits:
            habit_obj = next(h for h in self.tracker.habits if h.name == habit["name"])
            completions = self.tracker.storage.get_completions_for_habit(habit_obj.habit_id)
            dates = [datetime.fromisoformat(c[0]).date() for c in completions]
            streak = calculate_longest_streak(dates, habit_obj.periodicity)
            
            # Compare with expected longest streak
            if habit_obj.name == "Wash the dishes":
                self.assertEqual(streak, 28)
            elif habit_obj.name == "Wash the car":
                self.assertEqual(streak, 4)
            elif habit_obj.name == "Therapy online":
                self.assertEqual(streak, 14)
            elif habit_obj.name == "Weekly Coding Challenge":
                self.assertEqual(streak, 4)
            elif habit_obj.name == "Meditate":
                self.assertEqual(streak, 28)

if __name__ == "__main__":
    unittest.main()
