import unittest
from tracker import HabitTracker
from analytics import calculate_longest_streak
from test_data import predefined_habits

class TestHabitAnalytics(unittest.TestCase):

    def setUp(self):
        self.tracker = HabitTracker()
        for habit in predefined_habits:
            self.tracker.add_habit(
                habit["name"],
                habit["periodicity"],
                habit["completion_dates"]
            )

    def test_wash_the_dishes_streak(self):
        streak = self.tracker.get_streak("Wash the dishes")
        self.assertEqual(streak, 28)

    def test_wash_the_car_streak(self):
        streak = self.tracker.get_streak("Wash the car")
        self.assertEqual(streak, 4)

    def test_therapy_online_streak(self):
        streak = self.tracker.get_streak("Therapy online")
        self.assertEqual(streak, 14)

    def test_weekly_coding_streak(self):
        streak = self.tracker.get_streak("Weekly Coding Challenge")
        self.assertEqual(streak, 4)
    
    def test_meditate(self):
        streak = self.tracker.get_streak("Meditate")
        self.assertEqual(streak, 28)

if __name__ == "__main__":
    unittest.main()
