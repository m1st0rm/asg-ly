import tkinter as tk
from tkinter import font
from tkinter import ttk
from backend.department_management import get_departments


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
