import sqlite3
import os
from werkzeug.security import generate_password_hash

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    
    # Cria a tabela com TODAS as colunas que o sistema usa (incluindo datanasc)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            datanasc TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT NOT NULL,
            rg TEXT NOT NULL,
            endereco TEXT NOT NULL,
            numero TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            foto TEXT NOT NULL,
            observacao TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    
    # Verifica se já existe um admin, se não, cria um
    admin = conn.execute('SELECT * FROM users WHERE is_admin = 1').fetchone()
    if not admin:
        conn.execute('''
            INSERT INTO users (nome, sobrenome, datanasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, senha, foto, observacao, is_admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            'Admin', 
            'Sistema', 
            '2000-01-01', 
            '51999999999', 
            '00000000000', 
            '0000000000', 
            'Rua do Admin', 
            '0', 
            'Centro', 
            'Porto Alegre', 
            'RS', 
            'admin@senac.com', 
            generate_password_hash('admin123'), 
            'default.png', 
            'Usuario administrador criado automaticamente',
            1
        ))
    
    conn.commit()
    conn.close()

# Se este arquivo for executado diretamente, cria o banco
if __name__ == '__main__':
    init_db()
    print("Banco de dados criado/atualizado com sucesso!")