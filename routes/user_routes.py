from flask import Blueprint, render_template, request, session, flash
from models.user_model import get_user_by_id, update_user
from utils.decorators import login_required
import os
import uuid
from config import UPLOAD_FOLDER

bp = Blueprint('user', __name__)

@bp.route('/cursos')
def cursos():
    return render_template('cursos.html')

@bp.route('/cursos/informatica')
def curso_info():
    return render_template('cursoti.html')

@bp.route('/cursos/sistemas')
def curso_sistemas():
    return render_template('cursosistemas.html')

@bp.route('/cursos/administracao')
def curso_admin():
    return render_template('cursoadm.html')

@bp.route('/cursos/ia')
def curso_ia():
    return render_template('cursoia.html')

@bp.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@bp.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    user_id = session['user_id']

    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        data_nasc = request.form.get('data_nasc')
        telefone = request.form.get('telefone')
        cpf = request.form.get('cpf')
        rg = request.form.get('rg')
        endereco = request.form.get('endereco')
        numero = request.form.get('numero')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        email = request.form.get('email')
        file = request.files.get('foto')

        user = get_user_by_id(user_id)
        filename = user['foto']

        if file and file.filename != '':
            ext = file.filename.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        update_user(
            user_id, 
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
            filename
        )
        flash('Perfil atualizado com sucesso!')

    user = get_user_by_id(user_id)
    return render_template('perfil.html', user=user)