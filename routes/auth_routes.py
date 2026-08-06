from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, get_user_by_email
import os
from config import UPLOAD_FOLDER

bp = Blueprint('auth', __name__)

@bp.route('/check_email')
def check_email():
    email = request.args.get('email')
    user = get_user_by_email(email)
    return jsonify({'exists': bool(user)})

@bp.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        data_nasc = request.form.get('data_nasc')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        email = request.form.get('email')
        senha = request.form.get('senha')
        observacao = request.form.get('observacoes', '')
        file = request.files.get('foto')

        if get_user_by_email(email):
            flash('Email ja cadastrado')
            return redirect(url_for('auth.cadastro'))

        filename = 'default.png'
        if file and file.filename != '':
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        cpf = ''
        rg = ''

        create_user(
            nome, 
            sobrenome, 
            data_nasc, 
            telefone, 
            cpf, 
            rg, 
            endereco, 
            numero, 
            bairro, 
            cidade, 
            estado, 
            email, 
            generate_password_hash(senha), 
            filename, 
            observacao
        )
        flash('Cadastro realizado')
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = get_user_by_email(request.form.get('email'))

        if user and check_password_hash(user['senha'], request.form.get('senha')):
            session['user_id'] = user['id']

            if user['is_admin']:
                return redirect(url_for('admin.admin'))

            return redirect(url_for('user.perfil'))

        flash('Login invalido')

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear() 
    flash('Voce saiu da sua conta.')
    return redirect(url_for('auth.login'))