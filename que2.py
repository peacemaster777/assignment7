# Q2
import tkinter as tk
from tkinter import messagebox
import calendar

def show_calendar():
    year = year_entry.get()

    try:
        year = int(year)
        cal = calendar.calendar(year)
        calendar_text.delete("1.0", tk.END)
        calendar_text.insert(tk.END, cal)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")

window = tk.Tk()
window.title("Calendar Application")

year_label = tk.Label(window, text="Enter Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

show_calendar_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_calendar_button.pack()

calendar_text = tk.Text(window)
calendar_text.pack()

window.mainloop()