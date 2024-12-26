import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from backend.commentaries import get_commentaries_for_task, insert_commentary_for_task


def set_task_comment_button_state(task_comment_text_entry, task_comment_button):
    if not task_comment_text_entry.get():
        task_comment_button.config(state=tk.DISABLED)
    else:
        task_comment_button.config(state=tk.NORMAL)


def press_task_comment_button(user_id, task_id, task_comment_text_entry, update_table_method):
    status = insert_commentary_for_task(user_id, task_id, task_comment_text_entry.get())
    if status == 1:
        messagebox.showerror("Ошибка", "Непредвиденная ошибка.")
        return

    messagebox.showinfo('Успех', "Комментарий успешно добавлен!")
    update_table_method()


def open_comments_window(root, user_id, task_id):
    comments_window = tk.Toplevel()
    comments_window.title(f"Комментарии")
    comments_window.geometry("1500x800")

    root.withdraw()

    label_font = font.Font(family="Arial", size=12, weight="bold")
    button_font = font.Font(family="Arial", size=10, weight="bold")

    system_label = tk.Label(comments_window, text=f"Комментарии к задаче №{task_id}", font=label_font)
    system_label.pack(fill=tk.X, pady=5, padx=10)

    separator1 = ttk.Separator(comments_window, orient="horizontal")
    separator1.pack(fill=tk.X)

    frame = tk.Frame(comments_window)
    frame.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    separator2 = ttk.Separator(comments_window, orient="horizontal")
    separator2.pack(fill=tk.X)

    task_comment_label = tk.Label(comments_window, text="Добавление комментария к задаче", font=label_font)
    task_comment_label.pack(fill=tk.X, pady=5, padx=10)

    separator3 = ttk.Separator(comments_window, orient="horizontal")
    separator3.pack(fill=tk.X)

    task_comment_text_label = tk.Label(comments_window, text="Текст комментария:", font=label_font)
    task_comment_text_label.pack(fill=tk.X, pady=5, padx=10)

    task_comment_text_entry = tk.Entry(comments_window)
    task_comment_text_entry.pack(fill=tk.X, pady=5, padx=10)

    task_comment_button = tk.Button(comments_window, text="Добавить комментарий", font=button_font,
                                    command=lambda: press_task_comment_button(user_id, task_id, task_comment_text_entry, update_table))

    task_comment_button.pack(fill=tk.X, pady=5, padx=10)

    task_comment_text_entry.bind("<KeyRelease>", lambda e: set_task_comment_button_state(task_comment_text_entry, task_comment_button))

    def update_table():
        nonlocal user_id, task_id
        data = get_commentaries_for_task(user_id, task_id)

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

    def close_comments_window():
        comments_window.destroy()
        root.deiconify()

    comments_window.protocol("WM_DELETE_WINDOW", close_comments_window)

    update_table()


