import sqlite3
from config import DATABASE
from werkzeug.security import generate_password_hash


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            data_nasc TEXT,
            telefone TEXt,
            cpf TEXT UNIQUE,
            rg TEXT,
            endereco TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT,
            estado TEXT,
            email TEXT UNIQUE,
            senha TEXT,
            foto TEXT,
            observacao TEXT,
            is_admin INTEGER DEFAULT 0
        )
    """)

    conn.execute(
        """
        INSERT OR IGNORE INTO users (nome,email,senha,foto,is_admin)
        VALUES (?,?,?,?,1)
    """,
        ("Admin", "admin@gmail.com", generate_password_hash("123456"), "default.png"),
    )

    conn.commit()
    conn.close()
