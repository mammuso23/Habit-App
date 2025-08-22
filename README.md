<img width="830" height="200" alt="image" src="https://github.com/user-attachments/assets/accc11a9-465e-4537-af4c-69a00f6444f8" />

This is a habit tracker app that is not only technically sound but also practically helpful in promoting consistency, accountability, and self-reflection. 
The primary goal of this application is to allow users to: 
Define personal habits with a set frequency (daily or weekly), 
Mark them as completed within a given period, 
Monitor their consistency through calculated streaks, 
And analyse habit trends using core statistics. 
---
## 📂 Project Structure
habit_tracker/

- habit.py - Habit class
- tracker.py - HabitTracker class (manages habits)
- storage.py - Handles SQLite database
- analytics.py - Analytics (streaks, completions, stats)
- gui.py - GUI with CustomTkinter
- main.py - CLI-based interface
- db.sqlite3 - SQLite database (auto-created)
- README.md - Project documentation

## Features
- Add new habits (daily or weekly).
- View all habits in a list.
- Mark habits as complete.
- Delete habits you no longer need.
- View completions in a **weekly grid**.
- Analytics:
  - Longest streak (daily or weekly).
  - Total completions.
  - Last completed date.
- CLI and GUI

## ⚙️ Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/mammuso23/Habit-App.git
cd Habit-App
```
After having the repo on your machine, you should make sure you have the requirements installed. Assuming you have pip installed:
```bash
pip install -r requirements.txt
```
If don't have pip, you can install the libraries on requirements.txt one by one by following [this step by step tutorial](https://www.geeksforgeeks.org/python/how-to-install-python-libraries-without-using-the-pip-command/).
## 2. Usage
To run the CLI version:
```bash
python main.py
```
To run the GUI version:
```bash
python gui.py
```
## 3. Example of the CLI Output
==== Habit Tracker Menu ====
1. View Habits
2. Add New Habit
3. Mark Habit as Complete
4. View Weekly Habits
5. Delete Habit
6. View My Habit Stats
7. Exit
## 4. Database
The app uses SQLite (db.sqlite3) for persistence.
- Tables:
 - habits → stores habit info.
 - completions → stores completion logs.
## 5. How to use the app.
The habit tracker comes with **two interfaces**:
1. **The CLI (Command Line Interface)**
2. **The GUI (Graphical User Interface)**

## The CLI version
```bash
python main.py
```
- Option 1 → View all habits you’ve created.
- Option 2 → Add a new habit (you’ll be asked for name + periodicity: daily/weekly).
- Option 3 → Mark a habit as completed (logs a completion in the database).
- Option 4 → View your weekly tracker in a grid-like format.
- Option 5 → Delete a habit by its ID.
- Option 6 → View analytics for a habit (longest streak, total completions, last completed).
- Option 7 → Exit the app.
  
## The GUI version
```bash
python gui.py
```
You’ll see a window with:
- Habit Name field → type the habit you want to track.
- Periodicity dropdown → select "daily" or "weekly".
- Add Habit button → creates the habit and adds it to the list.
- Habit List → shows all habits with their IDs and periodicities.
- Grid Tracker → a 7-day grid where you can tick off completions using checkboxes.
- Dark Mode toggle → switch between light and dark themes.
