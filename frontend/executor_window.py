import tkinter as tk
from tkinter import ttk
from tkinter import font
from frontend.personal_info_window import open_personal_info_window
from frontend.tasks_for_executor_window import open_tasks_for_executor_window


def open_executor_window(root, user_id):
    executor_window = tk.Toplevel()
    executor_window.title("Панель исполнителя задач")
    executor_window.geometry("500x225")

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    root.withdraw()

    system_label = tk.Label(executor_window, text="Панель исполнителя задач", font=label_font)
    system_label.pack(fill=tk.X, pady=10, padx=10)

    separator1 = ttk.Separator(executor_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    look_personal_info_button = tk.Button(executor_window, text='Управление личной информацией', font=button_font, state=tk.NORMAL, command=lambda: open_personal_info_window(executor_window, user_id))
    look_personal_info_button.pack(fill=tk.X, pady=20, padx=10)

    separator2 = ttk.Separator(executor_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    manage_taks_button = tk.Button(executor_window, text='Управление поручениями', font=button_font, state=tk.NORMAL, command=lambda: open_tasks_for_executor_window(executor_window, user_id))
    manage_taks_button.pack(fill=tk.X, pady=20, padx=10)

    def close_executor_window():
        executor_window.destroy()
        root.deiconify()

    executor_window.protocol("WM_DELETE_WINDOW", close_executor_window)