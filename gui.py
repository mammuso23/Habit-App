import customtkinter as ctk
from tracker import HabitTracker
from datetime import datetime, timedelta
from tkinter import messagebox

ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Track My Habit📝")
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
        messagebox.showwarning(title="Input Error", message="Please enter both Habit Name and Periodicity.")

main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both")

title = ctk.CTkLabel(main_frame, text="Track My Habit 📝", font=("Arial", 20))
title.pack(pady=10)

frame = ctk.CTkFrame(main_frame)
frame.pack(pady=10, padx=10, fill="x")

def toggle_habit_completion(habit, day, checkbox):
    if checkbox.get():
        tracker.complete_habit(habit.habit_id, day)
    else:
        tracker.undo_completion(habit.habit_id, day)
    update_grid()

def toggle_mode():
    current = ctk.get_appearance_mode()
    if current == "Light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

mode_switch = ctk.CTkSwitch(app, text="Dark Mode", command=toggle_mode)
mode_switch.pack(pady=5)

def update_grid():
    for widget in grid_frame.winfo_children():
        widget.destroy()

    completions = tracker.get_completion_lookup()
    today = datetime.today().date()
    days = [(today - timedelta(days=i)).isoformat() for i in range(6, -1, -1)]

    grid_frame.grid_columnconfigure(0, weight=1)
    for i in range(1, len(days) + 1):
        grid_frame.grid_columnconfigure(i, weight=1)
    for row_index in range(len(tracker.habits) + 1):
        grid_frame.grid_rowconfigure(row_index, weight=1)

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

def delete_selected_habit():
    try:
        # Get the selected habit line (format: "ID. Name (periodicity)")
        selected_text = habit_listbox.get("sel.first", "sel.last").strip()
        if not selected_text:
            messagebox.showwarning(title="Selection Error", message="Please select a habit to delete.")
            return

        habit_id = int(selected_text.split(".")[0])
        tracker.delete_habit(habit_id)

        update_habit_list()
        update_grid()
        messagebox.showinfo(title="Deleted", message="Habit deleted successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Failed to delete habit.\n{e}")

entry_name = ctk.CTkEntry(frame, placeholder_text="Habit Name")
entry_name.grid(row=0, column=0, padx=5, pady=5)

periodicity_dropdown = ctk.CTkComboBox(frame, values=["daily", "weekly"])
periodicity_dropdown.set("daily")
periodicity_dropdown.grid(row=0, column=1, padx=5, pady=5)

add_button = ctk.CTkButton(frame, text="Add Habit", fg_color="#61afef", hover_color="#528ecc", command=add_habit)
add_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = ctk.CTkButton(
    frame,
    text="Delete Habit",
    fg_color="#e06c75",
    hover_color="#d45c67",
    command=delete_selected_habit
)
delete_button.grid(row=0, column=3, padx=5, pady=5)

habit_listbox = ctk.CTkTextbox(main_frame, state = "normal")
habit_listbox.pack(pady=10, padx=10, expand=True, fill="both")
habit_listbox.configure(state="disabled")

grid_frame = ctk.CTkFrame(main_frame)
grid_frame.pack(pady=10, padx=10, expand=True, fill="both")

update_habit_list()
update_grid()

app.mainloop()
