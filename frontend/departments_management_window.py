import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk
from frontend.helpers import is_positive_integer
from backend.department_management import (get_departments,
                                           add_department,
                                           update_department)


def set_add_department_button_state(add_department_name_entry, add_department_button):
    if not add_department_name_entry.get():
        add_department_button.config(state=tk.DISABLED)
    else:
        add_department_button.config(state=tk.NORMAL)


def set_update_department_button_state(update_department_id_entry, update_department_name_entry, update_department_button):
    if not update_department_id_entry.get() or not update_department_name_entry.get():
        update_department_button.config(state=tk.DISABLED)
    else:
        update_department_button.config(state=tk.NORMAL)


def insert_new_department(user_id, add_department_name_entry, update_table_method):
    status = add_department(user_id, add_department_name_entry.get())
    if status == 1:
        messagebox.showerror("Ошибка", "Отдел с таким именем уже существует.")
        return

    if status == 2:
        messagebox.showerror("Ошибка", "Произошла непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Новый отдел успешно добавлен.")
    update_table_method()


def update_department_info(user_id, update_department_id_entry, update_department_name_entry, update_table_method):
    if not is_positive_integer(update_department_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат ID отдела.")
        return
    status = update_department(user_id, update_department_id_entry.get(), update_department_name_entry.get())
    if status == 1:
        messagebox.showerror('Ошибка', "Отдела с указанным ID не существует.")
        return
    if status == 2:
        messagebox.showerror("Ошибка", "Отдел с таким именем уже существует.")
        return
    if status == 3:
        messagebox.showerror("Ошибка", "Произошла непредвиденная ошибка.")
        return

    messagebox.showinfo("Успех", "Отдел успешно переименован.")
    update_table_method()


def open_departments_management_window(root, user_id):
    departments_management_window = tk.Toplevel()
    departments_management_window.title("Управление отделами")
    departments_management_window.geometry("1500x800")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    system_label = tk.Label(departments_management_window, text="Панель управления отделами", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(departments_management_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    current_departments_label = tk.Label(departments_management_window, text="Таблица текущего состояния отделов", font=label_font)
    current_departments_label.pack(fill=tk.X, pady=5, padx=10)

    frame = tk.Frame(departments_management_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    separator2 = ttk.Separator(departments_management_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    add_department_label = tk.Label(departments_management_window, text="Добавление нового отдела", font=label_font)
    add_department_label.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(departments_management_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    add_department_name_label = tk.Label(departments_management_window, text="Имя нового отдела:", font=label_font)
    add_department_name_label.pack(fill=tk.X, pady=5, padx=10)

    add_department_name_entry = tk.Entry(departments_management_window)
    add_department_name_entry.pack(fill=tk.X, pady=5, padx=10)

    add_department_button = tk.Button(departments_management_window, text="Добавить отдел", font=button_font,
                                      command=lambda: insert_new_department(user_id, add_department_name_entry, update_table), state=tk.DISABLED)
    add_department_button.pack(fill=tk.X, pady=5, padx=10)

    separator4 = ttk.Separator(departments_management_window, orient="horizontal")
    separator4.pack(fill=tk.X)

    update_department_label = tk.Label(departments_management_window, text="Изменение существующего отдела", font=label_font)
    update_department_label.pack(fill=tk.X, pady=5, padx=10)

    separator5 = ttk.Separator(departments_management_window, orient="horizontal")
    separator5.pack(fill=tk.X)

    update_department_id_label = tk.Label(departments_management_window, text="ID отдела для изменения:", font=label_font)
    update_department_id_label.pack(fill=tk.X, pady=5, padx=10)

    update_department_id_entry = tk.Entry(departments_management_window)
    update_department_id_entry.pack(fill=tk.X, pady=5, padx=10)

    update_department_name_label = tk.Label(departments_management_window, text="Новое имя отдела:", font=label_font)
    update_department_name_label.pack(fill=tk.X, pady=5, padx=10)

    update_department_name_entry = tk.Entry(departments_management_window)
    update_department_name_entry.pack(fill=tk.X, pady=5, padx=10)

    update_department_button = tk.Button(departments_management_window, text="Изменить отдел", font=button_font,
                                         command=lambda: update_department_info(user_id, update_department_id_entry, update_department_name_entry, update_table), state=tk.DISABLED)
    update_department_button.pack(fill=tk.X, pady=5, padx=10)

    add_department_name_entry.bind("<KeyRelease>", lambda e: set_add_department_button_state(add_department_name_entry, add_department_button))
    update_department_id_entry.bind("<KeyRelease>", lambda e: set_update_department_button_state(update_department_id_entry, update_department_name_entry, update_department_button))
    update_department_name_entry.bind("<KeyRelease>", lambda e: set_update_department_button_state(update_department_id_entry, update_department_name_entry, update_department_button))

    def update_table():
        nonlocal user_id
        data = get_departments(user_id)

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

    def close_departments_management_window():
        departments_management_window.destroy()
        root.deiconify()

    departments_management_window.protocol("WM_DELETE_WINDOW", close_departments_management_window)

    update_table()
