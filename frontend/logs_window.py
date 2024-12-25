import tkinter as tk
from tkinter import font
from tkinter import ttk
from backend.action_history import get_action_history


def open_logs_window(root, user_id):
    logs_window = tk.Toplevel()
    logs_window.title('Логи действий')
    logs_window.geometry("1500x800")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")

    system_label = tk.Label(logs_window, text="Журнал действий пользователей", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(logs_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    frame = tk.Frame(logs_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    data = get_action_history(user_id)

    columns = list(data[0].keys())
    tree = ttk.Treeview(frame, columns=columns, show='headings',
                        yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    text_font = font.Font(family="TkDefaultFont")

    def calculate_width(text):
        return text_font.measure(text) + 20

    for col in columns:
        tree.heading(col, text=col)
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

    def close_logs_window():
        logs_window.destroy()
        root.deiconify()

    logs_window.protocol("WM_DELETE_WINDOW", close_logs_window)
