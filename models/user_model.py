from database import get_db_connection

def create_user(nome, sobrenome, data_nasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, senha, foto, observacao):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO users (nome, sobrenome, datanasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, senha, foto, observacao) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (nome, sobrenome, data_nasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, senha, foto, observacao)
    )
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email=?',(email,)).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id=?',(user_id,)).fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

def update_user(user_id, nome, sobrenome, data_nasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, foto):
    conn = get_db_connection()
    conn.execute('UPDATE users SET nome=?, sobrenome=?, datanasc=?, telefone=?, cpf=?, rg=?, endereco=?, numero=?, bairro=?, cidade=?, estado=?, email=?, foto=? WHERE id=?',
                 (nome, sobrenome, data_nasc, telefone, cpf, rg, endereco, numero, bairro, cidade, estado, email, foto, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id=?',(user_id,))
    conn.commit()
    conn.close()