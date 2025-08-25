from datetime import datetime

def calculate_longest_streak(dates, periodicity):
    if not dates:
        return 0

    streak = longest = 0
    previous = None
    sorted_dates = sorted(dates)

    for date in sorted_dates:
        if previous:
            delta_days = (date - previous).days
            if (
                (periodicity == "daily" and delta_days == 1) or
                (periodicity == "weekly" and delta_days <= 7)
            ):
                streak += 1
            else:
                streak = 1
        else:
            streak = 1

        longest = max(longest, streak)
        previous = date

    return longest
