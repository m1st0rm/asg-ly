import tkinter as tk
from tkinter import font
from tkinter import ttk
from frontend.login_window import open_login_window
from frontend.register_window import open_register_window


root = tk.Tk()
root.title("Система контроля поручений внутри организации")
root.geometry("500x200")

label_font = font.Font(family="Arial", size=12, weight="bold")
button_font = font.Font(family="Arial", size=10, weight="bold")

system_label = tk.Label(root, text="Система контроля поручений внутри организации", font=label_font)
system_label.pack(fill=tk.X, pady=20, padx=10)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill=tk.X)

login_button = tk.Button(root, text="Войти", font=button_font, command=lambda: open_login_window(root))
login_button.pack(fill=tk.X, pady=20, padx=10)

register_button = tk.Button(root, text="Зарегистрироваться", font=button_font, command=lambda: open_register_window(root))
register_button.pack(fill=tk.X, pady=20, padx=10)

root.mainloop()
