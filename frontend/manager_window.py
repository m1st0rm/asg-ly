import tkinter as tk
from tkinter import ttk
from tkinter import font
from frontend.personal_info_window import open_personal_info_window
from frontend.add_task_window import open_add_task_window
from frontend.tasks_for_manager_window import open_tasks_for_manager_window


def open_manager_window(root, user_id):
    manager_window = tk.Toplevel()
    manager_window.title("Панель координатора задач")
    manager_window.geometry("500x275")

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    root.withdraw()

    system_label = tk.Label(manager_window, text="Панель координатора задач", font=label_font)
    system_label.pack(fill=tk.X, pady=10, padx=10)

    separator1 = ttk.Separator(manager_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    look_personal_info_button = tk.Button(manager_window, text='Управление личной информацией', font=button_font, state=tk.NORMAL, command=lambda: open_personal_info_window(manager_window, user_id))
    look_personal_info_button.pack(fill=tk.X, pady=20, padx=10)

    separator2 = ttk.Separator(manager_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    add_task_button = tk.Button(manager_window, text='Добавить поручение', font=button_font, state=tk.NORMAL, command=lambda: open_add_task_window(manager_window, user_id))
    add_task_button.pack(fill=tk.X, pady=20, padx=10)

    separator3 = ttk.Separator(manager_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    manage_taks_button = tk.Button(manager_window, text='Управление поручениями', font=button_font, state=tk.NORMAL, command=lambda: open_tasks_for_manager_window(manager_window, user_id))
    manage_taks_button.pack(fill=tk.X, pady=20, padx=10)


    def close_manager_window():
        manager_window.destroy()
        root.deiconify()

    manager_window.protocol("WM_DELETE_WINDOW", close_manager_window)