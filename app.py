from flask import Flask, redirect, render_template, url_for, session  # importa flask
from database import init_db  # banco
from routes.auth_routes import bp as auth_bp  # rotas auth
from routes.user_routes import bp as user_bp  # rotas user
from routes.admin_routes import bp as admin_bp  # rotas admin
from models.user_model import get_user_by_id  # busca usuário
from config import SECRET_KEY  # config

app = Flask(__name__)  # cria app
app.secret_key = SECRET_KEY  # define chave

init_db()  # cria banco e admin

app.register_blueprint(auth_bp)  # registra auth
app.register_blueprint(user_bp)  # registra user
app.register_blueprint(admin_bp)  # registra admin


@app.route('/')  # rota inicial
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)  # roda sistema