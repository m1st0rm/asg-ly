import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from backend.tasks_executor import get_executor_tasks, update_task_executor_status
from frontend.helpers import is_positive_integer
from frontend.comments_window import open_comments_window


ALLOWED_TASKS = []

STATUSES = {
    "Не начата": 1,
    "В работе": 2,
    "Доработка": 3,
    "Выполнена": 4,
}


def set_task_change_button_state(task_change_id_entry, task_change_status_combobox, task_change_button):
    if not task_change_id_entry.get() or (task_change_status_combobox.get() == 'Выберите статус...'):
        task_change_button.config(state=tk.DISABLED)
    else:
        task_change_button.config(state=tk.NORMAL)


def set_task_comments_button_state(task_comments_id_entry, task_comments_button):
    if not task_comments_id_entry.get():
        task_comments_button.config(state=tk.DISABLED)
    else:
        task_comments_button.config(state=tk.NORMAL)


def press_task_change_button(user_id, task_change_id_entry, task_change_status_combobox, update_table_method):
    if not is_positive_integer(task_change_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат номера задачи.")
        return
    if int(task_change_id_entry.get()) not in ALLOWED_TASKS:
        messagebox.showerror("Ошибка", "Задачи с указанным номером не существует или вы не можете изменить её статус.")
        return

    task_id = task_change_id_entry.get()
    status_id = STATUSES[task_change_status_combobox.get()]

    exit_code = update_task_executor_status(user_id, task_id, status_id)
    if exit_code == 1:
        messagebox.showerror("Ошибка", "Непредвиденная ошибка.")
        return

    messagebox.showinfo('Успех', 'Статус задачи со стороны исполнителя успешно обновлён!')
    update_table_method()


def press_task_comments_button(root, user_id, task_comments_id_entry):
    if not is_positive_integer(task_comments_id_entry.get()):
        messagebox.showerror("Ошибка", "Неверный формат номера задачи.")
        return
    if int(task_comments_id_entry.get()) not in ALLOWED_TASKS:
        messagebox.showerror("Ошибка", "Задачи с указанным номером не существует или вы не можете писать к ней комментарии.")
        return

    task_id = int(task_comments_id_entry.get())
    open_comments_window(root, user_id, task_id)


def open_tasks_for_executor_window(root, user_id):
    global STATUSES
    tasks_window = tk.Toplevel()
    tasks_window.title("Панель управления задачами")
    tasks_window.geometry("1500x800")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    system_label = tk.Label(tasks_window, text="Панель управления задачами", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(tasks_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    current_tasks_label = tk.Label(tasks_window, text="Текущее состояние задач", font=label_font)
    current_tasks_label.pack(fill=tk.X, pady=5, padx=10)

    frame = tk.Frame(tasks_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    separator2 = ttk.Separator(tasks_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    task_change_label = tk.Label(tasks_window, text="Обновление статуса задачи", font=label_font)
    task_change_label.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(tasks_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    task_change_id_label = tk.Label(tasks_window, text="Номер задачи:", font=label_font)
    task_change_id_label.pack(fill=tk.X, pady=5, padx=10)

    task_change_id_entry = tk.Entry(tasks_window)
    task_change_id_entry.pack(fill=tk.X, pady=5, padx=10)

    task_change_status_label = tk.Label(tasks_window, text="Cтатус со стороны исполнителя:", font=label_font)
    task_change_status_label.pack(fill=tk.X, pady=5, padx=10)

    task_change_status_combobox = ttk.Combobox(tasks_window, values=list(STATUSES.keys()), state="readonly")
    task_change_status_combobox.set('Выберите статус...')
    task_change_status_combobox.pack(fill=tk.X, pady=5, padx=10)

    task_change_button = tk.Button(tasks_window, text="Обновить статус задачи", font=button_font,
                                   command=lambda: press_task_change_button(user_id, task_change_id_entry, task_change_status_combobox, update_table), state=tk.DISABLED)
    task_change_button.pack(fill=tk.X, pady=5, padx=10)

    separator4 = ttk.Separator(tasks_window, orient="horizontal")
    separator4.pack(fill=tk.X)

    task_comments_label = tk.Label(tasks_window, text='Комментарии к задаче', font=label_font)
    task_comments_label.pack(fill=tk.X, pady=5, padx=10)

    separator5 = ttk.Separator(tasks_window, orient="horizontal")
    separator5.pack(fill=tk.X)

    task_comment_id_label = tk.Label(tasks_window, text="Номер задачи:", font=label_font)
    task_comment_id_label.pack(fill=tk.X, pady=5, padx=10)

    task_comments_id_entry = tk.Entry(tasks_window)
    task_comments_id_entry.pack(fill=tk.X, pady=5, padx=10)

    task_comments_button = tk.Button(tasks_window, text='Открыть комментарии к задаче', font=button_font,
                                     command=lambda: press_task_comments_button(tasks_window, user_id, task_comments_id_entry), state=tk.DISABLED)
    task_comments_button.pack(fill=tk.X, pady=5, padx=10)

    task_change_id_entry.bind('<KeyRelease>', lambda e: set_task_change_button_state(task_change_id_entry, task_change_status_combobox, task_change_button))
    task_change_status_combobox.bind('<<ComboboxSelected>>', lambda e: set_task_change_button_state(task_change_id_entry, task_change_status_combobox, task_change_button))
    task_comments_id_entry.bind('<KeyRelease>', lambda e: set_task_comments_button_state(task_comments_id_entry, task_comments_button))

    def update_table():
        global ALLOWED_TASKS
        nonlocal user_id
        data = get_executor_tasks(user_id)

        for task in data:
            ALLOWED_TASKS.append(task['Номер задачи'])

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

    def close_tasks_window():
        tasks_window.destroy()
        root.deiconify()

    tasks_window.protocol("WM_DELETE_WINDOW", close_tasks_window)

    update_table()
