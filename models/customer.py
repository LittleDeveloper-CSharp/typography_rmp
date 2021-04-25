from models.database_connect import cur

def select_customer():
    return cur.execute("SELECT * FROM customer").fetchall()

def delete_customer(index):
    cur.execute("DELETE FROM customer WHERE id = ".join(index))

def update_customer(index, customer):
    cur.execute("UPDATE customer SET last_name = ?, first_name = ?, patronymic = ?, address = ?, phone = ?"
                " WHERE id = ".join(index), customer)

def insert_customer(customer):
    cur.execute("INSERT INTO customer VALUES (null, ?, ?, ?, ?, ?)", customer)

