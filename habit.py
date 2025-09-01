from datetime import datetime

class Habit:
    """Represents a habit with its properties and tracking functionality.

    Attributes:
    habit_id (int), name (str), periodicity ('daily' or 'weekly'), and created_at (str)
    """

    def __init__(self, habit_id: int, name: str, periodicity: str, created_at: str = None):
        """Initializes a new Habit instance.
        
        Args:
            habit_id (int), name (str), periodicity ('daily' or 'weekly'), and created_at (str)
        """
        self.habit_id = habit_id
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().isoformat()

    def __str__(self):
        return f"[{self.habit_id}]{self.name} ({self.periodicity})"
    
    def was_broken(self, completions):
        return len(completions) == 0

    def get_created_date(self):
        return self.created_at.split("T")[0]

    def get_total_completions(self, completions):
        return len(completions)

    def get_current_streak(self, completions):
        """Calculates the current streak of consecutive completions.
        
        Args:
            completions (list)
            
        Returns:
            int: Current streak length
        """
        if not completions:
            return 0

        dates = sorted(datetime.fromisoformat(c[0]).date() for c in completions)
        today = datetime.today().date()
        streak = 0

        for date in reversed (dates):
            delta = (today - date).days

            if self.periodicity == "daily":
                if delta == 0 or delta == 1:
                    streak += 1
                    today = date
                elif delta > 1:
                    break
            elif self.periodicity == "weekly":
                if delta <= 7:
                    streak += 1
                    today = date
                else:
                    break

        return streak
    
    def get_days_missed(self, completions):
        """Calculates how many days/weeks have been missed since the user last completed.
        
        Args:
            completions (list)
            
        Returns:
            int/str: Number of days/weeks missed, or 'Not Available' if no completions
        """
        if not completions:
            return "Not Available"

        last_completed = max(datetime.fromisoformat(c[0]).date() for c in completions)
        today = datetime.today().date()

        if self.periodicity == "daily":
            return (today - last_completed).days
        elif self.periodicity == "weekly":
            weeks_missed = (today - last_completed).days // 7
            return weeks_missed

        return "Not Available"
