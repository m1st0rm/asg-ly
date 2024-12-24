import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from backend.login import login
from frontend.helpers import validate_email


def set_login_button_state(entry_email, entry_password, login_button):
    if entry_email.get() and entry_password.get():
        login_button.config(state=tk.NORMAL)
    else:
        login_button.config(state=tk.DISABLED)


def login_command(entry_email, entry_password):
    email = entry_email.get()

    if not validate_email(email):
        messagebox.showerror("Ошибка", "Некорректный формат Email.")
        return

    password = entry_password.get()
    user = login(email, password)

    if user == 0:
        messagebox.showerror("Ошибка", "Учётная запись не существует или введены неправильные данные для входа.")
        return
    elif user == 1:
        messagebox.showerror("Ошибка", "Учётная запись деактивирована.\nДля активации свяжитесь с администратором.")
        return

    messagebox.showinfo("Успех", "Вы успешно авторизованы!")


def open_login_window(root):
    login_window = tk.Toplevel()
    login_window.title("Авторизация")
    login_window.geometry("500x250")

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    root.withdraw()

    system_label = tk.Label(login_window, text="Авторизация", font=label_font)
    system_label.pack(fill=tk.X, pady=10, padx=10)

    separator1 = ttk.Separator(login_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    label_email = tk.Label(login_window, text="Email:", font=label_font)
    label_email.pack(fill=tk.X, padx=10)

    entry_email = tk.Entry(login_window)
    entry_email.pack(fill=tk.X, pady=10, padx=10)

    label_password = tk.Label(login_window, text="Пароль:", font=label_font)
    label_password.pack(fill=tk.X, padx=10)

    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack(fill=tk.X, pady=10, padx=10)

    separator2 = ttk.Separator(login_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    login_button = tk.Button(login_window, text="Войти", font=button_font, command=lambda: login_command(entry_email, entry_password),
                             state=tk.DISABLED)
    login_button.pack(fill=tk.X, pady=20, padx=10)

    entry_email.bind("<KeyRelease>", lambda event: set_login_button_state(entry_email, entry_password, login_button))
    entry_password.bind("<KeyRelease>", lambda event: set_login_button_state(entry_email, entry_password, login_button))

    def close_login_window():
        login_window.destroy()
        root.deiconify()

    login_window.protocol("WM_DELETE_WINDOW", close_login_window)
