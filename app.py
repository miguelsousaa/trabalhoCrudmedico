from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a673e87911497f639bab03ad306d6bd56a6f36d3bcf5357197e1d6b740822f12'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/sousaConsultorio"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate

from models import Paciente, Consulta

db.init_app(app)
migrate = Migrate(app, db)

from modulos.pacientes.pacientes import bp_pacientes
app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
from modulos.consultas.consultas import bp_consultas
app.register_blueprint(bp_consultas, url_prefix='/consultas')

@app.route("/")
def index():
    return render_template("index.html")