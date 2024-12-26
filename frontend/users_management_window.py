import tkinter as tk
from tkinter import ttk
from tkinter import font
from frontend.helpers import is_positive_integer
from backend.users_management import get_users_ex_admin, get_roles_names, get_departments_names, update_user_active_status, update_user_role, update_user_department
from tkinter import messagebox


def set_update_active_status_button_state(update_active_status_user_id_entry, update_active_status_combobox, update_active_status_button):
    if not update_active_status_user_id_entry.get() or (update_active_status_combobox.get() == "Выберите статус учётной записи..."):
        update_active_status_button.config(state=tk.DISABLED)
    else:
        update_active_status_button.config(state=tk.NORMAL)


def set_update_role_button_state(update_role_user_id_entry, update_role_combobox, update_role_button):
    if not update_role_user_id_entry.get() or (update_role_combobox.get() == "Выберите роль учётной записи..."):
        update_role_button.config(state=tk.DISABLED)
    else:
        update_role_button.config(state=tk.NORMAL)


def set_update_department_button_state(update_department_user_id_entry, update_department_combobox, update_department_button):
    if not update_department_user_id_entry.get() or (update_department_combobox.get() == "Выберите отдел учётной записи..."):
        update_department_button.config(state=tk.DISABLED)
    else:
        update_department_button.config(state=tk.NORMAL)


def press_update_active_status_button(user_id, update_active_status_user_id_entry, update_active_status_combobox, update_table_method):
    if not is_positive_integer(update_active_status_user_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат ID отдела.")
        return

    if update_active_status_user_id_entry.get() == '1':
        messagebox.showerror("Ошибка", "Данные этого пользователя нельзя редактировать.")
        return

    status = update_user_active_status(user_id, update_active_status_user_id_entry.get(), update_active_status_combobox.get())

    if status == 1:
        messagebox.showerror('Ошибка', "Пользователя с указанным ID не существует.")
        return

    if status == 2:
        messagebox.showerror('Ошибка', "Непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Статус активности пользователя успешно изменён!")
    update_table_method()


def press_update_role_button(user_id, update_role_user_id_entry, update_role_combobox, update_table_method):
    if not is_positive_integer(update_role_user_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат ID отдела.")
        return
    if update_role_user_id_entry.get() == '1':
        messagebox.showerror("Ошибка", "Данные этого пользователя нельзя редактировать.")
        return

    status = update_user_role(user_id, update_role_user_id_entry.get(), update_role_combobox.get())

    if status == 1:
        messagebox.showerror('Ошибка', "Пользователя с указанным ID не существует.")
        return
    if status == 2:
        messagebox.showerror('Ошибка', "Данному пользователю нельзя изменить роль, так как он не выполнил все задачи на текущий момент.")
        return
    if status == 3:
        messagebox.showerror('Ошибка', "Непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Роль пользователя успешно изменена!")
    update_table_method()


def press_update_department_button(user_id, update_department_user_id_entry, update_department_combobox, update_table_method):
    if not is_positive_integer(update_department_user_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат ID отдела.")
        return
    if update_department_user_id_entry.get() == '1':
        messagebox.showerror("Ошибка", "Данные этого пользователя нельзя редактировать.")
        return

    status = update_user_department(user_id, update_department_user_id_entry.get(), update_department_combobox.get())
    if status == 1:
        messagebox.showerror('Ошибка', "Пользователя с указанным ID не существует.")
        return
    if status == 2:
        messagebox.showerror('Ошибка', "Непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Отдел пользователя успешно изменён!")
    update_table_method()


def open_users_management_window(root, user_id):
    users_management_window = tk.Toplevel()
    users_management_window.title("Управление отделами")
    users_management_window.geometry("1500x1000")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    system_label = tk.Label(users_management_window, text="Панель управления пользователями", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(users_management_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    current_departments_label = tk.Label(users_management_window, text="Таблица текущего состояния отделов", font=label_font)
    current_departments_label.pack(fill=tk.X, pady=5, padx=10)

    frame = tk.Frame(users_management_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    separator2 = ttk.Separator(users_management_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    update_active_status_label = tk.Label(users_management_window, text="Изменение статуса активности пользователя", font=label_font)
    update_active_status_label.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(users_management_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    update_active_status_user_id_label = tk.Label(users_management_window, text="ID пользователя для изменения:", font=label_font)
    update_active_status_user_id_label.pack(fill=tk.X, pady=5, padx=10)

    update_active_status_user_id_entry = tk.Entry(users_management_window)
    update_active_status_user_id_entry.pack(fill=tk.X, pady=5, padx=10)

    update_active_status_combo_label = tk.Label(users_management_window, text="Новый статус пользователя:", font=label_font)
    update_active_status_combo_label.pack(fill=tk.X, pady=5, padx=10)

    update_active_status_combobox = ttk.Combobox(users_management_window, values=['Активна', 'Неактивна'], state="readonly")
    update_active_status_combobox.set("Выберите статус учётной записи...")
    update_active_status_combobox.pack(fill=tk.X, pady=5, padx=10)

    update_active_status_button = tk.Button(users_management_window, text='Изменить статус пользователя', font=button_font,
                                            command=lambda: press_update_active_status_button(user_id, update_active_status_user_id_entry, update_active_status_combobox, update_table), state=tk.DISABLED)
    update_active_status_button.pack(fill=tk.X, pady=5, padx=10)

    separator4 = ttk.Separator(users_management_window, orient="horizontal")
    separator4.pack(fill=tk.X)

    update_role_label = tk.Label(users_management_window, text="Изменение роли пользователя", font=label_font)
    update_role_label.pack(fill=tk.X, pady=5, padx=10)

    separator5 = ttk.Separator(users_management_window, orient="horizontal")
    separator5.pack(fill=tk.X)

    update_role_user_id_label = tk.Label(users_management_window, text="ID пользователя для изменения:", font=label_font)
    update_role_user_id_label.pack(fill=tk.X, pady=5, padx=10)

    update_role_user_id_entry = tk.Entry(users_management_window)
    update_role_user_id_entry.pack(fill=tk.X, pady=5, padx=10)

    update_role_combo_label = tk.Label(users_management_window, text="Новая роль пользователя:", font=label_font)
    update_role_combo_label.pack(fill=tk.X, pady=5, padx=10)

    roles_for_combo = get_roles_names()
    update_role_combobox = ttk.Combobox(users_management_window, values=roles_for_combo, state="readonly")
    update_role_combobox.set("Выберите роль учётной записи...")
    update_role_combobox.pack(fill=tk.X, pady=5, padx=10)

    update_role_button = tk.Button(users_management_window, text='Изменить роль пользователя', font=button_font,
                                            command=lambda: press_update_role_button(user_id, update_role_user_id_entry, update_role_combobox, update_table), state=tk.DISABLED)
    update_role_button.pack(fill=tk.X, pady=5, padx=10)

    separator6 = ttk.Separator(users_management_window, orient="horizontal")
    separator6.pack(fill=tk.X)

    update_department_label = tk.Label(users_management_window, text="Изменение отдела пользователя", font=label_font)
    update_department_label.pack(fill=tk.X, pady=5, padx=10)

    separator7 = ttk.Separator(users_management_window, orient="horizontal")
    separator7.pack(fill=tk.X)

    update_department_user_id_label = tk.Label(users_management_window, text="ID пользователя для изменения:", font=label_font)
    update_department_user_id_label.pack(fill=tk.X, pady=5, padx=10)

    update_department_user_id_entry = tk.Entry(users_management_window)
    update_department_user_id_entry.pack(fill=tk.X, pady=5, padx=10)

    update_department_combo_label = tk.Label(users_management_window, text="Новый отдел пользователя:", font=label_font)
    update_department_combo_label.pack(fill=tk.X, pady=5, padx=10)

    departments_for_combo = get_departments_names()
    update_department_combobox = ttk.Combobox(users_management_window, values=departments_for_combo, state="readonly")
    update_department_combobox.set("Выберите отдел учётной записи...")
    update_department_combobox.pack(fill=tk.X, pady=5, padx=10)

    update_department_button = tk.Button(users_management_window, text='Изменить отдел пользователя', font=button_font,
                                   command=lambda: press_update_department_button(user_id, update_department_user_id_entry, update_department_combobox, update_table), state=tk.DISABLED)
    update_department_button.pack(fill=tk.X, pady=5, padx=10)

    update_active_status_user_id_entry.bind("<KeyRelease>",
                                            lambda e: set_update_active_status_button_state(update_active_status_user_id_entry, update_active_status_combobox, update_active_status_button))
    update_active_status_combobox.bind("<<ComboboxSelected>>",
                                       lambda e: set_update_active_status_button_state(update_active_status_user_id_entry ,update_active_status_combobox, update_active_status_button))
    update_role_user_id_entry.bind("<KeyRelease>",
                                   lambda e: set_update_role_button_state(update_role_user_id_entry, update_role_combobox, update_role_button))
    update_role_combobox.bind("<<ComboboxSelected>>",
                              lambda e: set_update_role_button_state(update_role_user_id_entry, update_role_combobox, update_role_button))
    update_department_user_id_entry.bind("<KeyRelease>",
                                         lambda e: set_update_department_button_state(update_department_user_id_entry, update_department_combobox, update_department_button))
    update_department_combobox.bind("<<ComboboxSelected>>",
                                    lambda e: set_update_department_button_state(update_department_user_id_entry, update_department_combobox, update_department_button))

    def update_table():
        nonlocal user_id
        data = get_users_ex_admin(user_id)

        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Scrollbar):
                continue
            widget.destroy()

        columns = list(data[0].keys())

        tree = ttk.Treeview(frame, columns=columns, show='headings',
                            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        text_font = font.Font(family="TkDefaultFont")

        def calculate_width(text):
            nonlocal text_font
            return text_font.measure(text) + 20

        for col in columns:
            tree.heading(col, text=col, anchor=tk.W)
            max_width_data = max(calculate_width(str(row[col])) for row in data)
            max_width_column = calculate_width(col)
            max_width = max([max_width_data, max_width_column])
            tree.column(col, width=max_width, anchor=tk.W)

        for row in data:
            values = tuple(row[col] for col in columns)
            tree.insert('', tk.END, values=values)

        tree.pack(fill=tk.BOTH, expand=True)

        scrollbar_y.config(command=tree.yview)
        scrollbar_x.config(command=tree.xview)

    def close_users_management_window():
        users_management_window.destroy()
        root.deiconify()

    users_management_window.protocol("WM_DELETE_WINDOW", close_users_management_window)

    update_table()

