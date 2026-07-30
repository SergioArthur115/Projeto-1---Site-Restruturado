from flask import Blueprint, render_template, request, session
from models.user_model import get_user_by_id, update_user
from utils.decorators import login_required
import os
import uuid  # gerar nome único
from config import UPLOAD_FOLDER

bp = Blueprint('user', __name__)

# Adicione ao final do arquivo routes/user_routes.py

@bp.route('/cursos')
def cursos():
    return render_template('pages/cursos.html')  

@bp.route('/cursos/informatica')
def curso_info():
    return render_template('pages/cursoinfo.html')

@bp.route('/cursos/sistemas')
def curso_sistemas():
    return render_template('pages/cursosistemas.html')

@bp.route('/cursos/administracao')
def curso_admin():
    return render_template('pages/cursoadmin.html')

@bp.route('/cursos/ia')
def curso_ia():
    return render_template('pages/cursointeligencia.html')

@bp.route('/localizacao')
def localizacao():
    return render_template('pages/localizacao.html')

@bp.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    user_id = session['user_id']

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        file = request.files.get('foto')

        user = get_user_by_id(user_id)

        filename = user['foto']

        # nome único imagem
        if file and file.filename != '':
            ext = file.filename.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        update_user(user_id, nome, email, filename)


    user = get_user_by_id(user_id)
    return render_template('perfil.html', user=user)

