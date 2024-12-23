import tkinter as tk
from tkinter import messagebox
from backend.register import register
from frontend.helpers import validate_email

def set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button):
    if entry_first_name.get() and entry_last_name.get() and entry_email.get() and entry_password.get() and entry_confirm_password.get():
        register_button.config(state=tk.NORMAL)
    else:
        register_button.config(state=tk.DISABLED)


def register_command(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password):
    email = entry_email.get()

    if not validate_email(email):
        messagebox.showerror("Ошибка", "Некорректный формат Email.")
        return

    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("Ошибка", "Пароли не совпадают.")
        return

    status = register(first_name, last_name, email, password)
    if status == 0:
        messagebox.showerror("Ошибка", "Пользователь с таким Email уже существует.")
        return
    elif status == 1:
        messagebox.showerror("Ошибка", "Произошла непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Регистрация прошла успешно!")


def open_register_window(root):
    register_window = tk.Toplevel()
    register_window.title("Регистрация")
    register_window.geometry("300x400")

    root.withdraw()

    label_first_name = tk.Label(register_window, text="Имя:")
    label_first_name.pack(pady=5)

    entry_first_name = tk.Entry(register_window)
    entry_first_name.pack(pady=5)

    label_last_name = tk.Label(register_window, text="Фамилия:")
    label_last_name.pack(pady=5)

    entry_last_name = tk.Entry(register_window)
    entry_last_name.pack(pady=5)

    label_email = tk.Label(register_window, text="Email:")
    label_email.pack(pady=5)

    entry_email = tk.Entry(register_window)
    entry_email.pack(pady=5)

    label_password = tk.Label(register_window, text="Пароль:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack(pady=5)

    label_confirm_password = tk.Label(register_window, text="Подтвердите пароль:")
    label_confirm_password.pack(pady=5)

    entry_confirm_password = tk.Entry(register_window, show="*")
    entry_confirm_password.pack(pady=5)

    register_button = tk.Button(register_window, text="Зарегистрироваться",
                                command=lambda: register_command(entry_first_name, entry_last_name, entry_email,
                                                         entry_password, entry_confirm_password), state=tk.DISABLED)
    register_button.pack(pady=10)

    entry_first_name.bind("<KeyRelease>", lambda event: set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button))
    entry_last_name.bind("<KeyRelease>", lambda event: set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button))
    entry_email.bind("<KeyRelease>", lambda event: set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button))
    entry_password.bind("<KeyRelease>", lambda event: set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button))
    entry_confirm_password.bind("<KeyRelease>", lambda event: set_register_button_state(entry_first_name, entry_last_name, entry_email, entry_password, entry_confirm_password, register_button))

    def close_register_window():
        register_window.destroy()
        root.deiconify()

    register_window.protocol("WM_DELETE_WINDOW", close_register_window)
