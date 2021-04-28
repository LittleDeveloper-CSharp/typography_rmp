from models.database_connect import cur

def authorization(login, password):
    text_command = "SELECT post FROM user WHERE login = '" + login + "' and password = '" + password + "'"
    post = cur.execute(text_command).fetchone()
    if post is None:
        return False, 0
    return len(post) != 0, post[0]