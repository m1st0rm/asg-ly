import tkinter as tk
from frontend.login_window import open_login_window
from frontend.register_window import open_register_window


root = tk.Tk()
root.title("Главное окно")
root.geometry("300x200")

login_button = tk.Button(root, text="Войти", command=lambda: open_login_window(root))
login_button.pack(pady=20)

register_button = tk.Button(root, text="Зарегистрироваться", command=lambda: open_register_window(root))
register_button.pack(pady=20)

root.mainloop()
