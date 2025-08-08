import customtkinter as ctk
from tracker import HabitTracker
from datetime import datetime, timedelta

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Track My Habit")
app.geometry("700x600")

tracker = HabitTracker("habits.db")

def update_habit_list():
    habit_listbox.configure(state="normal")
    habit_listbox.delete("1.0", ctk.END)
    for habit in tracker.habits:
        habit_listbox.insert(ctk.END, f"{habit.habit_id}. {habit.name} ({habit.periodicity})\n")
    habit_listbox.configure(state="disabled")

def add_habit():
    name = entry_name.get().strip()
    periodicity = periodicity_dropdown.get()

    if name and periodicity:
        tracker.add_habit(name, periodicity)
        entry_name.delete(0, ctk.END)
        update_habit_list()
        update_grid()
    else:
        ctk.CTkMessagebox(title="Input Error", message="Please enter both Habit Name and Periodicity.")

def toggle_habit_completion(habit, day, checkbox):
    if checkbox.get():
        tracker.complete_habit(habit.habit_id, day)
    else:
        tracker.undo_completion(habit.habit_id, day)
    update_grid()

def update_grid():
    for widget in grid_frame.winfo_children():
        widget.destroy()

    completions = tracker.get_completion_lookup()
    today = datetime.today().date()
    days = [(today - timedelta(days=i)).isoformat() for i in range(6, -1, -1)]

    ctk.CTkLabel(grid_frame, text="Habit ↓ / Day →").grid(row=0, column=0, padx=5, pady=5)
    for i, d in enumerate(days):
        ctk.CTkLabel(grid_frame, text=d[-5:]).grid(row=0, column=i + 1, padx=5, pady=5)

    for row_index, habit in enumerate(tracker.habits, start=1):
        ctk.CTkLabel(grid_frame, text=habit.name).grid(row=row_index, column=0, padx=5, pady=5)
        completed_days = completions.get(habit.habit_id, [])

        for col_index, day in enumerate(days):
            is_checked = day in completed_days
            checkbox = ctk.CTkCheckBox(
                grid_frame,
                text="",
                checkbox_height=20,
                checkbox_width=20,
                command=lambda d=day, h=habit, cb_var=None: toggle_habit_completion(h, d, checkbox)
            )
            checkbox.grid(row=row_index, column=col_index + 1, padx=5, pady=5)
            checkbox.select() if is_checked else checkbox.deselect()

def toggle_theme():
    current_mode = ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark" if current_mode == "light" else "light")

title = ctk.CTkLabel(app, text="My Habit Tracker", font=("Arial", 20))
title.pack(pady=10)

theme_switch = ctk.CTkSwitch(app, text="Dark Mode", command=toggle_theme)
theme_switch.pack(pady=5)

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="x")

entry_name = ctk.CTkEntry(frame, placeholder_text="Habit Name")
entry_name.grid(row=0, column=0, padx=5, pady=5)

periodicity_dropdown = ctk.CTkComboBox(frame, values=["daily", "weekly"])
periodicity_dropdown.set("daily")
periodicity_dropdown.grid(row=0, column=1, padx=5, pady=5)

add_button = ctk.CTkButton(frame, text="Add Habit", fg_color="#61afef", hover_color="#528ecc", command=add_habit)
add_button.grid(row=0, column=2, padx=5, pady=5)

habit_listbox = ctk.CTkTextbox(app, width=500, height=150)
habit_listbox.pack(pady=10)
habit_listbox.configure(state="disabled")

grid_frame = ctk.CTkFrame(app)
grid_frame.pack(pady=10)

update_habit_list()
update_grid()

app.mainloop()
