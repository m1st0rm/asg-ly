import tkinter as tk
from tkinter import messagebox
from backend.login import login


def validate_input_login(entry_email, entry_password, login_button):
    if entry_email.get() and entry_password.get():
        login_button.config(state=tk.NORMAL)
    else:
        login_button.config(state=tk.DISABLED)


def login_command(entry_email, entry_password):
    email = entry_email.get()
    password = entry_password.get()
    user = login(email, password)

    if user == 0:
        messagebox.showerror("Ошибка", "Учётная запись не существует или введены неправильные данные для входа.")
    elif user == 1:
        messagebox.showerror("Ошибка", "Учётная запись деактивирована.\nДля активации свяжитесь с администратором.")
    else:
        messagebox.showinfo("Успех", user)


def open_login_window(root):
    login_window = tk.Toplevel()
    login_window.title("Авторизация")
    login_window.geometry("300x200")

    root.withdraw()

    label_email = tk.Label(login_window, text="Email:")
    label_email.pack(pady=5)

    entry_email = tk.Entry(login_window)
    entry_email.pack(pady=5)

    label_password = tk.Label(login_window, text="Пароль:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack(pady=5)

    login_button = tk.Button(login_window, text="Войти", command=lambda: login_command(entry_email, entry_password),
                             state=tk.DISABLED)
    login_button.pack(pady=10)

    entry_email.bind("<KeyRelease>", lambda event: validate_input_login(entry_email, entry_password, login_button))
    entry_password.bind("<KeyRelease>", lambda event: validate_input_login(entry_email, entry_password, login_button))

    def close_login_window():
        login_window.destroy()
        root.deiconify()

    login_window.protocol("WM_DELETE_WINDOW", close_login_window)
