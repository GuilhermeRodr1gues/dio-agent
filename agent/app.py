import sqlite3

def auth_login(user,password):
    conection = sqlite3.connect('banco_de_dados.db')
    cursor = conection.cursor()
    
    # Placeholders '?' tratam user e password como DADOS, jamais como
    # parte da estrutura SQL. Injeção não é mais possível.
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"

    cursor.execute(query, (user, password))
    result = cursor.fetchone()
    conection.close()
    
    if result:
        return "Acess done!"
    else:
        return "Acess denied!"