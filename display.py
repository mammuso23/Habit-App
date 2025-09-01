from datetime import datetime, timedelta

def build_weekly_grid(habits, completions_lookup):
    """Displays the table of all habits with their status."""
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    week_dates = [(start_of_week + timedelta(days=i)).date() for i in range(7)]

    print("\n==== Weekly Habit Tracker ====\n")

    day_labels = [d.strftime("%a") for d in week_dates]
    print("Habit Name".ljust(20), end=" ")
    for day in day_labels:
        print(day.center(5), end=" ")
    print("\n" + "-" * (20 + 7 * 6))

    for habit in habits:
        habit_id = habit["habit_id"]
        habit_name = habit["name"]
        row = habit_name.ljust(20)

        completed_dates = completions_lookup.get(habit_id, [])
        completed_dates = [datetime.fromisoformat(d).date() for d in completed_dates]

        for day in week_dates:
            if day in completed_dates:
                row += "  ✅  "
            else:
                row += "  ⬜  "

        print(row)
