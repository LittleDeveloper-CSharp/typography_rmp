from models.database_connect import cur

def select_typography():
    return cur.execute().fetchall()

def select_typography_by_name(name):
    return cur.execute().fetchall()

def delete_typography(index):
    cur.execute()

def update_typography(index, typography):
    cur.execute()

def insert_typography():
    cur.execute()
