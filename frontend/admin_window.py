import tkinter as tk
from tkinter import ttk
from tkinter import font
from frontend.personal_info_window import open_personal_info_window


def open_admin_window(root, user_id):
    admin_window = tk.Toplevel()
    admin_window.title("Админ-панель")
    admin_window.geometry("500x350")

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    root.withdraw()

    system_label = tk.Label(admin_window, text="Панель администратора", font=label_font)
    system_label.pack(fill=tk.X, pady=10, padx=10)

    separator1 = ttk.Separator(admin_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    look_personal_info_button = tk.Button(admin_window, text='Управление личной информацией', font=button_font, state=tk.NORMAL, command=lambda: open_personal_info_window(admin_window, user_id))
    look_personal_info_button.pack(fill=tk.X, pady=20, padx=10)

    separator2 = ttk.Separator(admin_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    look_logs_button = tk.Button(admin_window, text="Посмотреть логи", font=button_font, state=tk.NORMAL)
    look_logs_button.pack(fill=tk.X, pady=20, padx=10)

    separator3 = ttk.Separator(admin_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    manage_users_button = tk.Button(admin_window, text="Управление пользователями", font=button_font, state=tk.NORMAL)
    manage_users_button.pack(fill=tk.X, pady=20, padx=10)

    separator4 = ttk.Separator(admin_window, orient="horizontal")
    separator4.pack(fill=tk.X)

    manage_departments_button = tk.Button(admin_window, text="Управление отделами", font=button_font, state=tk.NORMAL)
    manage_departments_button.pack(fill=tk.X, pady=20, padx=10)

    def close_admin_window():
        admin_window.destroy()
        root.deiconify()

    admin_window.protocol("WM_DELETE_WINDOW", close_admin_window)