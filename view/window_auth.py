from models.authorization import authorization
import view.window_customer
from tkinter import Button, Label, Entry, Tk, Frame, messagebox, Toplevel

def click_auth():
    if authorization(login_entry.get(), password_entry.get()):
        Toplevel(view.window_customer)
        messagebox.showinfo(title="Все хорошо", message="Пользователь найден")
    else:
        messagebox.showerror(title="Ошибка", message="Пользователь не найден")


root_auth = Tk()
root_auth.wm_title("Авторизация")
root_auth.geometry("300x150")
root_auth.minsize(300, 150)
root_auth.resizable(False, False)
root_auth.grid_columnconfigure(0, weight=1)

frame_login = Frame()
Label(frame_login, text="Логин").grid(row=0)
login_entry = Entry(frame_login)
login_entry.grid(row=1)
frame_login.grid(row=0, column=0)

frame_password = Frame()
Label(frame_password, text="Пароль").grid(row=0)
password_entry = Entry(frame_password)
password_entry.grid(row=1)
frame_password.grid(row=1, column=0)

Button(text="Вход", command=click_auth).grid(row=2)

root_auth.mainloop()
