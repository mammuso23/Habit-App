import unittest
from habit import Habit
from tracker import HabitTracker

class TestHabit(unittest.TestCase):
    def test_habit_creation(self):
        habit = Habit(1, "Exercise", "daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")

    def test_edit_habit(self):
        habit = Habit(1, "Exercise", "daily")
        habit.name = "Meditation"
        habit.periodicity = "weekly"
        self.assertEqual(habit.name, "Meditation")
        self.assertEqual(habit.periodicity, "weekly")

    def test_tracker_add_delete_habit(self):
        tracker = HabitTracker(":memory:")
        tracker.add_habit("Exercise", "daily")
        self.assertEqual(len(tracker.habits), 1)
        self.assertEqual(tracker.habits[0].name, "Exercise")

        habit_id = tracker.habits[0].habit_id
        tracker.delete_habit(habit_id)
        self.assertEqual(len(tracker.habits), 0)

if __name__ == "__main__":
    unittest.main()
