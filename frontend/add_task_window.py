import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from backend.add_task import get_users_to_add_task, insert_new_task
from frontend.helpers import is_positive_integer

ALLOWED_USERS = []

PRIORITIES = {
    "Низкий": 1,
    "Средний": 2,
    "Высокий": 3,
    "Критичный": 4
}

TASK_TYPES = {
    "Разработка новых решений": 1,
    "Написание нового функционала": 2,
    "Написание тестов для функционала": 3,
    "Поиск и починка бага": 4,
    "Ревью кода": 5,
    "Рефакторинг кода": 6,
    "Написание документации": 7,
}


def set_add_task_button_state(add_task_name_entry, add_task_desc_entry, add_task_executor_id_entry, add_task_days_entry, add_task_priority_combobox, add_task_type_combobox, add_task_button):
    if not add_task_name_entry.get() or not add_task_desc_entry.get() or not add_task_days_entry.get() or not add_task_executor_id_entry.get() or (add_task_priority_combobox.get() == 'Выберите приоритет...') or (add_task_type_combobox.get() == 'Выберите тип задачи...'):
        add_task_button.config(state=tk.DISABLED)
    else:
        add_task_button.config(state=tk.NORMAL)


def press_add_task_button(user_id, add_task_name_entry, add_task_desc_entry, add_task_executor_id_entry, add_task_days_entry, add_task_priority_combobox, add_task_type_combobox):
    if not is_positive_integer(add_task_executor_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат ID исполнителя.")
        return
    if int(add_task_executor_id_entry.get()) not in ALLOWED_USERS:
        messagebox.showerror("Ошибка", "Исполнителя с указанным ID не существует или вы не можете назначить ему задачу.")
        return
    if not is_positive_integer(add_task_days_entry.get()) or int(add_task_days_entry.get()) == 0:
        messagebox.showerror("Ошибка", "Неверное количество дней на исполнение.")
        return

    task_name = add_task_name_entry.get()
    task_desc = add_task_desc_entry.get()
    task_executor_id = add_task_executor_id_entry.get()
    task_days = int(add_task_days_entry.get())
    created_by_user_id = user_id
    priority_id = PRIORITIES[add_task_priority_combobox.get()]
    task_type_id = TASK_TYPES[add_task_type_combobox.get()]

    status = insert_new_task(task_name, task_desc, task_executor_id, task_days, created_by_user_id, priority_id, task_type_id)

    if status == 1:
        messagebox.showerror("Ошибка", "Непредвиденная ошибка.")
        return

    messagebox.showinfo('Успех', "Задача успешно добавлена!")


def open_add_task_window(root, user_id):
    add_task_window = tk.Toplevel()
    add_task_window.title("Добавление новой задачи")
    add_task_window.geometry("1500x800")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    system_label = tk.Label(add_task_window, text="Панель добавления новой задачи", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(add_task_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    users_label = tk.Label(add_task_window, text="Исполнители для назначения задачи", font=label_font)
    users_label.pack(fill=tk.X, pady=5, padx=10)

    frame = tk.Frame(add_task_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    separator2 = ttk.Separator(add_task_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    add_task_label = tk.Label(add_task_window, text="Добавление новой задачи", font=label_font)
    add_task_label.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(add_task_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    add_task_name_label = tk.Label(add_task_window, text="Имя задачи:", font=label_font)
    add_task_name_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_name_entry = tk.Entry(add_task_window)
    add_task_name_entry.pack(fill=tk.X, pady=5, padx=10)

    add_task_desc_label = tk.Label(add_task_window, text="Описание задачи:", font=label_font)
    add_task_desc_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_desc_entry = tk.Entry(add_task_window)
    add_task_desc_entry.pack(fill=tk.X, pady=5, padx=10)

    add_task_executor_id_label = tk.Label(add_task_window, text="ID исполнителя:", font=label_font)
    add_task_executor_id_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_executor_id_entry = tk.Entry(add_task_window)
    add_task_executor_id_entry.pack(fill=tk.X, pady=5, padx=10)

    add_task_days_label = tk.Label(add_task_window, text="Количество дней на исполнение:", font=label_font)
    add_task_days_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_days_entry = tk.Entry(add_task_window)
    add_task_days_entry.pack(fill=tk.X, pady=5, padx=10)

    add_task_priority_label = tk.Label(add_task_window, text="Приоритет задачи: ", font=label_font)
    add_task_priority_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_priority_combobox = ttk.Combobox(add_task_window, values=list(PRIORITIES.keys()), state="readonly")
    add_task_priority_combobox.set('Выберите приоритет...')
    add_task_priority_combobox.pack(fill=tk.X, pady=5, padx=10)

    add_task_type_label = tk.Label(add_task_window, text="Тип задачи: ", font=label_font)
    add_task_type_label.pack(fill=tk.X, pady=5, padx=10)

    add_task_type_combobox = ttk.Combobox(add_task_window, values=list(TASK_TYPES.keys()), state="readonly")
    add_task_type_combobox.set('Выберите тип задачи...')
    add_task_type_combobox.pack(fill=tk.X, pady=5, padx=10)

    separator4 = ttk.Separator(add_task_window, orient="horizontal")
    separator4.pack(fill=tk.X)

    add_task_button = tk.Button(add_task_window, text='Добавить задачу', font=button_font, command=lambda: press_add_task_button(user_id, add_task_name_entry, add_task_desc_entry, add_task_executor_id_entry, add_task_days_entry, add_task_priority_combobox, add_task_type_combobox), state=tk.DISABLED)
    add_task_button.pack(fill=tk.X, pady=5, padx=10)

    add_task_name_entry.bind("<KeyRelease>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))

    add_task_desc_entry.bind("<KeyRelease>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))
    add_task_executor_id_entry.bind("<KeyRelease>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))
    add_task_days_entry.bind("<KeyRelease>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))
    add_task_priority_combobox.bind("<<ComboboxSelected>>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))
    add_task_type_combobox.bind("<<ComboboxSelected>>",
                             lambda e: set_add_task_button_state(add_task_name_entry, add_task_desc_entry,
                                                                 add_task_executor_id_entry, add_task_days_entry,
                                                                 add_task_priority_combobox, add_task_type_combobox,
                                                                 add_task_button))


    def update_table():
        global ALLOWED_USERS
        nonlocal user_id
        data = get_users_to_add_task(user_id)

        for user in data:
            ALLOWED_USERS.append(user['ID исполнителя'])

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

    def close_add_task_window():
        add_task_window.destroy()
        root.deiconify()

    add_task_window.protocol("WM_DELETE_WINDOW", close_add_task_window)

    update_table()
