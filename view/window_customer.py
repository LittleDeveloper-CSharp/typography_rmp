import models.customer
from tkinter import Entry, END, Button, Label, Frame, VERTICAL
from tkinter.ttk import Treeview, Scrollbar

index_customer = 0

list_customer = ()

def fill_tree_view():
    global list_customer
    list_customer = models.customer.select_customer()
    for item in list_customer:
        tree_view_customer.insert("", "end", values=item)

def filter_by_name(event, name):
    final_filter()

def filter_by_patronymic(event, patronymic):
    final_filter()

def filter_by_last_name(event, last_name):
    final_filter()

def final_filter():
    global list_customer

def accept_action():
    action = bt_accept['text']
    if action == "Добавить":
        models.customer.insert_customer(list())
    else:
        models.customer.update_customer(index_customer, list())
    fill_tree_view()

def delete_action():
    models.customer.delete_customer(index_customer)
    fill_tree_view()


frame_output_info = Frame()

frame_first_name_search = Frame(frame_output_info)
first_name_search_entry = Entry(frame_output_info)
first_name_search_entry.grid(row=0, column=0)


columns = ("1", "2", "3", "4", "5", "6")
tree_view_customer = Treeview(frame_output_info, show="headings", columns=columns,
                              displaycolumns=("2", "3", "4", "5", "6"))
tree_view_customer.heading("2", text="Фамилия")
tree_view_customer.heading("3", text="Имя")
tree_view_customer.heading("4", text="Отчество")
tree_view_customer.heading("5", text="Адрес")
tree_view_customer.heading("6", text="Телефон")

ysb = Scrollbar(orient=VERTICAL, command=tree_view_customer.yview)
tree_view_customer.config(yscroll=ysb.set)

tree_view_customer.grid(column=0)
frame_output_info.grid(row=0, column=0)

frame_for_add = Frame()

frame_last_name = Frame(frame_for_add)
Label(frame_last_name, text="Фамилия").grid(row=0)
last_name_entry = Entry(frame_last_name)
last_name_entry.grid(row=1)
frame_last_name.grid(row=0)

frame_first_name = Frame(frame_for_add)
Label(frame_first_name, text="Имя").grid(row=0)
first_name_entry = Entry(frame_first_name)
first_name_entry.grid(row=1)
frame_first_name.grid(row=1)

frame_patronymic = Frame(frame_for_add)
Label(frame_patronymic, text="Отчество").grid(row=0)
patronymic_entry = Entry(frame_patronymic)
patronymic_entry.grid(row=1)
frame_patronymic.grid(row=2)

frame_address = Frame(frame_for_add)
Label(frame_address, text="Адрес").grid(row=0)
address_entry = Entry(frame_address)
address_entry.grid(row=1)
frame_address.grid(row=3)

frame_phone = Frame(frame_for_add)
Label(frame_phone, text="Телефон").grid(row=0)
phone_entry = Entry(frame_phone)
phone_entry.grid(row=1)
frame_phone.grid(row=4)

bt_accept = Button(frame_for_add, text="Добавить")
bt_accept.grid(row=5)
Button(frame_for_add, text="Удалить").grid(row=6)

frame_for_add.grid(row=0, column=1)

fill_tree_view()
