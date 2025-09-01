from datetime import datetime, timedelta

def calculate_longest_streak(habit):
    """Calculates the current streak for a given habit."""
    if not habit.completion_dates:
        return 0
    
    dates = sorted([cd.date() if isinstance(cd, datetime) else cd for cd in habit.completion_dates])
    
    if habit.periodicity == "daily":
        return calculate_daily_streak(dates)
    elif habit.periodicity == "weekly":
        return calculate_weekly_streak(dates)
    else:
        return 0

def calculate_daily_streak(dates):
    """Calculate streak for daily habits"""
    if not dates:
        return 0
    
    streak = 1
    longest = 1
    dates = sorted(dates)
    
    for i in range(1, len(dates)):
        if (dates[i] - dates[i-1]).days == 1:
            streak += 1
        else:
            streak = 1 
        longest = max(longest, streak)
    
    return longest

def calculate_weekly_streak(dates):
    """Calculate streak for weekly habits"""
    if not dates:
        return 0
    
    streak = 1
    longest = 1
    dates = sorted(dates)
    
    for i in range(1, len(dates)):
        days_diff = (dates[i] - dates[i-1]).days
        if days_diff <= 7:
            streak += 1
        else:
            streak = 1 
        longest = max(longest, streak)
    
    return longest
