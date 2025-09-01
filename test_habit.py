import unittest
from datetime import datetime, timedelta, date
from habit import Habit

class TestHabit(unittest.TestCase):
    """Test cases for the Habit class using your actual code structure."""

    def test_habit_initialization(self):
        """Test that a Habit object is initialized correctly."""
        habit = Habit(habit_id=1, name="Test Habit", periodicity="daily")
        
        self.assertEqual(habit.habit_id, 1)
        self.assertEqual(habit.name, "Test Habit")
        self.assertEqual(habit.periodicity, "daily")
        self.assertIsNotNone(habit.created_at)

    def test_habit_string_representation(self):
        """Test the string representation of a Habit object."""
        habit = Habit(habit_id=1, name="Meditate", periodicity="daily")
        expected_str = "[1]Meditate (daily)"
        self.assertEqual(str(habit), expected_str)

    def test_daily_streak_calculation(self):
        """Test streak calculation for a daily habit."""
        habit = Habit(habit_id=1, name="Daily Exercise", periodicity="daily")
        
        today = datetime.now()
        completions = [
            [today.isoformat()],
            [(today - timedelta(days=1)).isoformat()],
            [(today - timedelta(days=2)).isoformat()],
            [(today - timedelta(days=3)).isoformat()],
        ]
        
        streak = habit.get_current_streak(completions)
        self.assertEqual(streak, 4, f"Expected 4-day streak, got {streak}")

    def test_weekly_streak_calculation(self):
        """Test streak calculation for a weekly habit."""
        habit = Habit(habit_id=2, name="Weekly Review", periodicity="weekly")
        
        today = datetime.now()
        completions = [
            [today.isoformat()],
            [(today - timedelta(weeks=1)).isoformat()],
            [(today - timedelta(weeks=2)).isoformat()],
        ]
        
        streak = habit.get_current_streak(completions)
        self.assertEqual(streak, 3, f"Expected 3-week streak, got {streak}")

    def test_empty_completions(self):
        """Test that streak is 0 when there are no completions."""
        habit = Habit(habit_id=3, name="No Completions", periodicity="daily")
        completions = []
        
        streak = habit.get_current_streak(completions)
        self.assertEqual(streak, 0, f"Expected 0 streak for no completions, got {streak}")

    def test_was_broken_method(self):
        """Test the was_broken method."""
        habit = Habit(habit_id=4, name="Test Broken", periodicity="daily")
        
        self.assertTrue(habit.was_broken([]))
        
        self.assertFalse(habit.was_broken([["2023-01-01T00:00:00"]]))

if __name__ == '__main__':
    unittest.main()
