from flask import Flask, redirect, render_template, url_for, session
from database import init_db
from routes.auth_routes import bp as auth_bp
from routes.user_routes import bp as user_bp
from routes.admin_routes import bp as admin_bp
from models.user_model import get_user_by_id
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Isso aqui cria o banco de dados com as colunas corretas
init_db() 

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)