from models.database_connect import cur

def authorization(login, password):
    text_command = "SELECT count(*) FROM user WHERE login = '" + login + "' and password = '" + password + "'"
    return cur.execute(text_command).fetchone()[0] != 0
