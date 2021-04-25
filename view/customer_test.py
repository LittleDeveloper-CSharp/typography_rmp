import models.customer
from tkinter import Entry, END, Button, Label, Frame, VERTICAL
from tkinter.ttk import Treeview, Scrollbar

class CustomerWindow:
    def fill_tree_view(self):
        self.list_customer = models.customer.select_customer()
        for item in self.list_customer:
            self.tree_view_customer.insert("", "end", values=item)

    def filter_by_name(self, event, name):
        self.final_filter()

    def filter_by_patronymic(self, event, patronymic):
        self.final_filter()

    def filter_by_last_name(self, event, last_name):
        self.final_filter()

    @staticmethod
    def final_filter():
        global list_customer
        a = 23

    def accept_action(self):
        action = self.bt_accept['text']
        if action == "Добавить":
            models.customer.insert_customer(list())
        else:
            models.customer.update_customer(self.index_customer, list())
        self.fill_tree_view()

    def delete_action(self):
        models.customer.delete_customer(self.index_customer)
        self.fill_tree_view()

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.index_customer = 0

        self.list_customer = ()
        self.frame_output_info = Frame()

        self.frame_first_name_search = Frame(self.frame_output_info)
        self.first_name_search_entry = Entry(self.frame_output_info)
        self.first_name_search_entry.grid(row=0, column=0)

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

        self.bt_accept = Button(self.frame_for_add, text="Добавить")
        self.bt_accept.grid(row=5)
        Button(self.frame_for_add, text="Удалить").grid(row=6)

        self.frame_for_add.grid(row=0, column=1)

        self.fill_tree_view()
