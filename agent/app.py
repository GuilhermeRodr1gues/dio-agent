import sqlite3
import hashlib
import base64
import os

ITERACOES = 100_000


def _gerar_hash(password):
    """Gera um sal aleatorio e devolve 'salt_b64$hash_b64'."""
    salt = os.urandom(16)
    derived = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, ITERACOES
    )
    return base64.b64encode(salt).decode("ascii") + "$" + base64.b64encode(
        derived
    ).decode("ascii")


def _verificar_senha(password, salt_b64, hash_b64):
    """Compara a senha recebida com o hash armazenado (mesmo sal)."""
    salt = base64.b64decode(salt_b64)
    expected = base64.b64decode(hash_b64)
    derived = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, ITERACOES
    )
    return derived == expected


def auth_login(user, password):
    conection = sqlite3.connect('banco_de_dados.db')
    try:
        cursor = conection.cursor()

        # Busca apenas o hash salvo do usuario (consulta parametrizada)
        cursor.execute(
            "SELECT password FROM usuarios WHERE username = ?",
            (user,),
        )
        row = cursor.fetchone()

        if row is None:
            return "Acess denied!"

        salt_b64, hash_b64 = row[0].split("$")
        return (
            "Acess done!"
            if _verificar_senha(password, salt_b64, hash_b64)
            else "Acess denied!"
        )
    finally:
        conection.close()


def registar_usuario(user, password):
    """Guarda a senha com sal (sozinho, para nao expor hexadecimais)."""
    conection = sqlite3.connect('banco_de_dados.db')
    try:
        cursor = conection.cursor()
        hash_salt = _gerar_hash(password)
        cursor.execute(
            "INSERT INTO usuarios (username, password) VALUES (?, ?)",
            (user, hash_salt),
        )
        conection.commit()
        return "Usuário criado."
    finally:
        conection.close()