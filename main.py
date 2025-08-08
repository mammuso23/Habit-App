from tracker import HabitTracker
from display import build_weekly_grid
from analytics import calculate_longest_streak
from datetime import datetime

def display_menu():
    print("<<<Let's Track Your Habits>>>")
    print("1. View Habits")
    print("2. Add A New Habit")
    print("3. Mark Your Habit as Complete")
    print("4. View Weekly Habits")
    print("5. Delete My Habit")
    print("6. View My Habit Stat")
    print("7. Exit")

def list_habits(habits):
    if not habits:
        print("There are no habits found.")
    for habit in habits:
        print(f"{habit.habit_id}. {habit.name} ({habit.periodicity})")

def main():
    tracker = HabitTracker("habits.db")

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            list_habits(tracker.habits)

        elif choice == '2':
            name = input("Enter your habit: ")
            periodicity = input("Enter periodicity (daily/weekly): ").lower()
            if periodicity not in ["daily", "weekly"]:
                print("Invalid periodicity.")
                continue
            tracker.add_habit(name, periodicity)
            print(f"Habit '{name}' has been added.")

        elif choice == '3':
            try:
                habit_id = int(input("Enter the ID of the habit you completed: "))
                tracker.mark_complete(habit_id)
                print("Marked as complete.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            completions = tracker.get_completion_lookup()
            habits = tracker.habits
            build_weekly_grid([h.__dict__ for h in habits], completions)

        elif choice == '5':
            list_habits(tracker.habits)
            try:
                habit_id = int(input("Enter the ID of the habit to delete: "))
                tracker.delete_habit(habit_id)
                print("Habit deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '6':
            list_habits(tracker.habits)
            try:
                habit_id = int(input("Enter the ID of the habit to analyze: "))
                habit = next((h for h in tracker.habits if h.habit_id == habit_id), None)

                if habit:
                    completions = tracker.storage.get_completions_for_habit(habit_id)
                    dates = [datetime.fromisoformat(c[0]).date() for c in completions]

                    if not dates:
                        print(f"\nAnalytics for '{habit.name}':")
                        print("  ➤ No completions recorded.\n")
                    else:
                        longest = calculate_longest_streak(dates, habit.periodicity)
                        print(f"\nAnalytics for '{habit.name}':")
                        print(f"  ➤ Longest Streak: {longest} days")
                        print(f"  ➤ Total Completions: {len(dates)}")
                        print(f"  ➤ Last Completed: {max(dates)}\n")
                else:
                    print("Habit not found.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '7':
            print("Goodbye. Remeber To Create Healthy Habits!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
