from models.authorization import authorization
from view.customer_test import CustomerWindow
from tkinter import Button, Label, Entry, Tk, Frame, messagebox, Toplevel


class AuthorizationWindow:
    def click_auth(self):
        if authorization(self.login_entry.get(), self.password_entry.get()):
            messagebox.showinfo(title="Все хорошо", message="Пользователь найден")
        else:
            messagebox.showerror(title="Ошибка", message="Пользователь не найден")

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.wm_title("Авторизация")
        self.master.geometry("300x150")
        self.master.minsize(300, 150)
        self.master.resizable(False, False)
        self.master.grid_columnconfigure(0, weight=1)

        self.frame_login = Frame()
        Label(self.frame_login, text="Логин").grid(row=0)
        self.login_entry = Entry(self.frame_login)
        self.login_entry.grid(row=1)
        self.frame_login.grid(row=0, column=0)

        self.frame_password = Frame()
        Label(self.frame_password, text="Пароль").grid(row=0)
        self.password_entry = Entry(self.frame_password)
        self.password_entry.grid(row=1)
        self.frame_password.grid(row=1, column=0)

        Button(text="Вход", command=self.click_auth).grid(row=2)

def main():
    root = Tk()
    app = AuthorizationWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()