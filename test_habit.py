import unittest
from habit import Habit

class TestHabit(unittest.TestCase):
    def test_habit_creation(self):
        habit = Habit("Exercise", "daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")

    def test_edit_habit(self):
        habit = Habit("Exercise", "daily")
        habit.name = "Meditation"
        habit.periodicity = "weekly"
        self.assertEqual(habit.name, "Meditation")
        self.assertEqual(habit.periodicity, "weekly")

    def test_delete_habit(self):
        habit = Habit("Exercise", "daily")
        habit_name = habit.name 
        del habit
        self.assertIsNone(habit_name)  

if __name__ == "__main__":
    unittest.main()