import sqlite3
import hashlib
def auth_login(user,password):
    conection = sqlite3.connect('banco_de_dados.db')
    cursor = conection.cursor()
    
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (user, pass_hash))

    result = cursor.fetchone()
    conection.close()

    if result:
        return "Acess done!"
    else:
        return "Acess denied!"