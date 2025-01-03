import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from backend.personal_info import get_personal_info_by_user_id, update_personal_info_by_user_id
from backend.helpers import hash_data
from frontend.helpers import validate_email


def set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button):
    if current_password_entry.get() and new_password_entry.get() and new_password_confirm_entry.get():
        password_change_status = 1
    elif not current_password_entry.get() and not new_password_entry.get() and not new_password_confirm_entry.get():
        password_change_status = 2
    else:
        password_change_status = 0

    if new_first_name_entry.get() or new_last_name_entry.get() or new_email_entry.get():
        other_change_status = 1
    else:
        other_change_status = 0

    if other_change_status == 0 and password_change_status == 0:
        make_update_button.config(state=tk.DISABLED)
    if other_change_status == 0 and password_change_status == 1:
        make_update_button.config(state=tk.NORMAL)
    if other_change_status == 0 and password_change_status == 2:
        make_update_button.config(state=tk.DISABLED)
    if other_change_status == 1 and password_change_status == 0:
        make_update_button.config(state=tk.DISABLED)
    if other_change_status == 1 and password_change_status == 1:
        make_update_button.config(state=tk.NORMAL)
    if other_change_status == 1 and password_change_status == 2:
        make_update_button.config(state=tk.NORMAL)


def update_personal_info(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, current_user, update_window_method):
    if not new_first_name_entry.get():
        new_first_name = current_user['first_name']
    else:
        new_first_name = new_first_name_entry.get()

    if not new_last_name_entry.get():
        new_last_name = current_user['last_name']
    else:
        new_last_name = new_last_name_entry.get()

    if not new_email_entry.get():
        new_email = current_user['email']
    else:
        if not validate_email(new_email_entry.get()):
            messagebox.showerror("Ошибка", "Некорректный формат Email.")
            return

        new_email = new_email_entry.get()

    if not current_password_entry.get() and not new_password_entry.get() and not new_password_confirm_entry.get():
        hashed_password = current_user['hashed_password']
    else:
        if hash_data(current_password_entry.get()) != current_user["hashed_password"]:
            messagebox.showerror("Ошибка", "Текущий пароль указан неверно.")
            return
        if new_password_entry.get() != new_password_confirm_entry.get():
            messagebox.showerror("Ошибка", "Новые пароли не совпадают.")
            return

        hashed_password = hash_data(new_password_entry.get())

    status = update_personal_info_by_user_id(current_user['user_id'], new_first_name, new_last_name, new_email, hashed_password)

    if status == 0:
        messagebox.showerror("Ошибка", "Пользователь с таким Email уже существует.")
        return

    if status == 1:
        messagebox.showerror("Ошибка", "Непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Персональные данные успешно обновлены.")
    update_window_method()


def open_personal_info_window(root, user_id):
    current_user = None
    personal_info_window = tk.Toplevel()
    personal_info_window.title("Управление личной информацией")
    personal_info_window.geometry("650x875")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")
    hint_font = font.Font(family="Arial", size=8, weight="normal")

    system_label = tk.Label(personal_info_window, text="Управление личной информацией", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(personal_info_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    hint_label = tk.Label(personal_info_window, text='Оставьте поле пустым, если не хотите менять связанную с ним информацию', font=hint_font)
    hint_label.pack(fill=tk.X, pady=5, padx=10)

    separator2 = ttk.Separator(personal_info_window, orient="horizontal")
    separator2.pack(fill=tk.X)
    # ------------------------------------------------------------------------------------------
    first_name_label = tk.Label(personal_info_window, font=label_font)
    first_name_label.pack(fill=tk.X, pady=5, padx=10)

    new_first_name_label = tk.Label(personal_info_window, text='Введите новое имя:', font=label_font)
    new_first_name_label.pack(fill=tk.X, pady=5, padx=10)

    new_first_name_entry = tk.Entry(personal_info_window)
    new_first_name_entry.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(personal_info_window, orient="horizontal")
    separator3.pack(fill=tk.X)
    # ------------------------------------------------------------------------------------------
    last_name_label = tk.Label(personal_info_window, font=label_font)
    last_name_label.pack(fill=tk.X, pady=5, padx=10)

    new_last_name_label = tk.Label(personal_info_window, text='Введите новую фамилию:', font=label_font)
    new_last_name_label.pack(fill=tk.X, pady=5, padx=10)

    new_last_name_entry = tk.Entry(personal_info_window)
    new_last_name_entry.pack(fill=tk.X, pady=5, padx=10)

    separator4 = ttk.Separator(personal_info_window, orient="horizontal")
    separator4.pack(fill=tk.X)
    # ------------------------------------------------------------------------------------------
    email_label = tk.Label(personal_info_window, font=label_font)
    email_label.pack(fill=tk.X, pady=10, padx=10)

    new_email_label = tk.Label(personal_info_window, text='Введите новый Email:', font=label_font)
    new_email_label.pack(fill=tk.X, pady=5, padx=10)

    new_email_entry = tk.Entry(personal_info_window)
    new_email_entry.pack(fill=tk.X, pady=5, padx=10)

    separator5 = ttk.Separator(personal_info_window, orient="horizontal")
    separator5.pack(fill=tk.X)
    # ------------------------------------------------------------------------------------------
    password_label = tk.Label(personal_info_window, text='Текущий пароль: ********', font=label_font)
    password_label.pack(fill=tk.X, pady=5, padx=10)

    current_password_label = tk.Label(personal_info_window, text='Введите текущий пароль:', font=label_font)
    current_password_label.pack(fill=tk.X, pady=5, padx=10)

    current_password_entry = tk.Entry(personal_info_window, show='*')
    current_password_entry.pack(fill=tk.X, pady=5, padx=10)

    new_password_label = tk.Label(personal_info_window, text='Введите новый пароль:', font=label_font)
    new_password_label.pack(fill=tk.X, pady=5, padx=10)

    new_password_entry = tk.Entry(personal_info_window, show='*')
    new_password_entry.pack(fill=tk.X, pady=5, padx=10)

    new_password_confirm_label = tk.Label(personal_info_window, text='Подтвердите новый пароль:', font=label_font)
    new_password_confirm_label.pack(fill=tk.X, pady=5, padx=10)

    new_password_confirm_entry = tk.Entry(personal_info_window, show='*')
    new_password_confirm_entry.pack(fill=tk.X, pady=5, padx=10)

    separator6 = ttk.Separator(personal_info_window, orient="horizontal")
    separator6.pack(fill=tk.X)

    make_update_button = tk.Button(personal_info_window, text='Обновить личную информацию', font=button_font,
                                   command=lambda: update_personal_info(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, current_user, update_window), state=tk.DISABLED)
    make_update_button.pack(fill=tk.X, pady=5, padx=10)

    separator7 = ttk.Separator(personal_info_window, orient="horizontal")
    separator7.pack(fill=tk.X)
    # ------------------------------------------------------------------------------------------
    id_label = tk.Label(personal_info_window, font=label_font)
    id_label.pack(fill=tk.X, pady=5, padx=10)

    separator8 = ttk.Separator(personal_info_window, orient="horizontal")
    separator8.pack(fill=tk.X)

    role_label = tk.Label(personal_info_window, font=label_font)
    role_label.pack(fill=tk.X, pady=5, padx=10)

    separator9 = ttk.Separator(personal_info_window, orient="horizontal")
    separator9.pack(fill=tk.X)

    department_label = tk.Label(personal_info_window, font=label_font)
    department_label.pack(fill=tk.X, pady=5, padx=10)

    separator10 = ttk.Separator(personal_info_window, orient="horizontal")
    separator10.pack(fill=tk.X)

    status_label = tk.Label(personal_info_window, font=label_font)
    status_label.pack(fill=tk.X, pady=5, padx=10)

    separator11 = ttk.Separator(personal_info_window, orient="horizontal")
    separator11.pack(fill=tk.X)

    create_timestamp_label = tk.Label(personal_info_window, font=label_font)
    create_timestamp_label.pack(fill=tk.X, pady=5, padx=10)

    separator12 = ttk.Separator(personal_info_window, orient="horizontal")
    separator12.pack(fill=tk.X)

    last_update_timestamp_label = tk.Label(personal_info_window, font=label_font)
    last_update_timestamp_label.pack(fill=tk.X, pady=5, padx=10)

    new_first_name_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))
    new_last_name_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))
    new_email_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))
    current_password_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))
    new_password_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))
    new_password_confirm_entry.bind("<KeyRelease>", lambda e: set_make_update_button_state(new_first_name_entry, new_last_name_entry, new_email_entry, current_password_entry, new_password_entry, new_password_confirm_entry, make_update_button))

    def update_window():
        nonlocal current_user
        current_user = get_personal_info_by_user_id(user_id)

        first_name_label.config(text=f"Текущее имя: {current_user['first_name']}")
        last_name_label.config(text=f"Текущая фамилия: {current_user['last_name']}")
        email_label.config(text=f"Текущий Email: {current_user['email']}")
        id_label.config(text=f"ID учётной записи: {current_user['user_id']}")
        role_label.config(text=f"Текущая роль: {current_user['role']}")
        department_label.config(text=f"Текущий отдел: {current_user['department']}")
        if current_user['is_active'] is True:
            status_label.config(text="Текущий статус учётной записи: Активна")
        else:
            status_label.config(text="Текущий статус учётной записи: Неактивна")
        create_timestamp_label.config(text=f"Дата и время создания учётной записи: {current_user['created_at'].strftime("%Y-%m-%d %H:%M:%S")}")
        last_update_timestamp_label.config(text=f"Дата и время последнего изменения учётной записи: {current_user['updated_at'].strftime("%Y-%m-%d %H:%M:%S")}")

    update_window()

    def close_personal_info_window():
        personal_info_window.destroy()
        root.deiconify()

    personal_info_window.protocol("WM_DELETE_WINDOW", close_personal_info_window)