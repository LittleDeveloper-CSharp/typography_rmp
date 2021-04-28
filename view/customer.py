import models.customer
from tkinter import Entry, END, Button, Label, Frame, VERTICAL
from tkinter.ttk import Treeview, Scrollbar

class CustomerWindow:

    def clear_tree_view(self):
        self.tree_view_customer.delete(*self.tree_view_customer.get_children())

    def fill_tree_view(self):
        self.clear_tree_view()
        self.list_customer = models.customer.select_customer()
        for item in self.list_customer:
            self.tree_view_customer.insert("", "end", values=item)

    def click_back(self):
        self.clear_entry()
        self.bt_accept['text'] = "Добавить"
        self.bt_back.grid_forget()

    def clear_entry(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.patronymic_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.phone_entry.delete(0, END)

    def select_item(self,event):
        self.customer = self.tree_view_customer.selection()[0]
        self.customer = self.tree_view_customer.item(self.customer, option="values")
        self.bt_accept['text'] = "Изменить"
        self.bt_back.grid(row=7)
        self.fill_entry()

    def create_customer(self):
        return (self.first_name_entry.get(),
        self.last_name_entry.get(),
        self.patronymic_entry.get(),
        self.address_entry.get(),
        self.phone_entry.get())

    def fill_entry(self):
        self.clear_entry()
        customer = self.customer
        self.index_customer = self.customer[0]
        self.first_name_entry.insert(0, customer[1])
        self.last_name_entry.insert(0, customer[2])
        self.patronymic_entry.insert(0, customer[3])
        self.address_entry.insert(0, customer[4])
        self.phone_entry.insert(0, customer[5])

    @staticmethod
    def final_filter():
        global list_customer
        a = 23

    def accept_action(self):
        action = self.bt_accept['text']
        if action == "Добавить":
            models.customer.insert_customer(self.create_customer())
        else:
            models.customer.update_customer(self.index_customer, self.create_customer())
        self.fill_tree_view()
        self.click_back()

    def delete_action(self):
        models.customer.delete_customer(self.index_customer)
        self.fill_tree_view()
        self.click_back()

    def __init__(self, master):
        self.customer = ()
        self.master = master
        self.frame = Frame(self.master)
        self.index_customer = 0

        self.list_customer = ()
        self.frame_output_info = Frame()

        #   Фильтрация
        #   <------------------------------------------------------------>

        self.frame_first_name_search = Frame(self.frame_output_info)
        self.first_name_search_entry = Entry(self.frame_output_info)
        self.first_name_search_entry.grid(row=0, column=0)

        #   <------------------------------------------------------------>

        #   Сортировка
        #   <------------------------------------------------------------>

        #   <------------------------------------------------------------>
        self.columns = ("1", "2", "3", "4", "5", "6")
        self.tree_view_customer = Treeview(self.frame_output_info, show="headings", columns=self.columns,
                                           displaycolumns=("2", "3", "4", "5", "6"))
        self.tree_view_customer.heading("2", text="Фамилия")
        self.tree_view_customer.heading("3", text="Имя")
        self.tree_view_customer.heading("4", text="Отчество")
        self.tree_view_customer.heading("5", text="Адрес")
        self.tree_view_customer.heading("6", text="Телефон")

        self.ysb = Scrollbar(orient=VERTICAL, command=self.tree_view_customer.yview)
        self.tree_view_customer.config(yscroll=self.ysb.set)

        self.tree_view_customer.bind("<<TreeviewSelect>>", self.select_item)

        self.tree_view_customer.grid(column=0)
        self.frame_output_info.grid(row=0, column=0)

        self.frame_for_add = Frame()

        self.frame_last_name = Frame(self.frame_for_add)
        Label(self.frame_last_name, text="Фамилия").grid(row=0)
        self.last_name_entry = Entry(self.frame_last_name)
        self.last_name_entry.grid(row=1)
        self.frame_last_name.grid(row=0)

        self.frame_first_name = Frame(self.frame_for_add)
        Label(self.frame_first_name, text="Имя").grid(row=0)
        self.first_name_entry = Entry(self.frame_first_name)
        self.first_name_entry.grid(row=1)
        self.frame_first_name.grid(row=1)

        self.frame_patronymic = Frame(self.frame_for_add)
        Label(self.frame_patronymic, text="Отчество").grid(row=0)
        self.patronymic_entry = Entry(self.frame_patronymic)
        self.patronymic_entry.grid(row=1)
        self.frame_patronymic.grid(row=2)

        self.frame_address = Frame(self.frame_for_add)
        Label(self.frame_address, text="Адрес").grid(row=0)
        self.address_entry = Entry(self.frame_address)
        self.address_entry.grid(row=1)
        self.frame_address.grid(row=3)

        self.frame_phone = Frame(self.frame_for_add)
        Label(self.frame_phone, text="Телефон").grid(row=0)
        self.phone_entry = Entry(self.frame_phone)
        self.phone_entry.grid(row=1)
        self.frame_phone.grid(row=4)

        self.bt_accept = Button(self.frame_for_add, text="Добавить", command=self.accept_action)
        self.bt_accept.grid(row=5)
        Button(self.frame_for_add, text="Удалить", command=self.delete_action).grid(row=6)

        self.bt_back = Button(self.frame_for_add, text="Отмена", command=self.click_back)

        self.frame_for_add.grid(row=0, column=1)

        self.fill_tree_view()
