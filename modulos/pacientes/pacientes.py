from flask import Blueprint, render_template, request, redirect, flash
from models import Paciente
from database import db

bp_pacientes = Blueprint('pacientes', __name__, template_folder="templates")

@bp_pacientes.route("/")
def index():
    p = Paciente.query.all()
    return render_template("pacientes.html", dados=p)


@bp_pacientes.route("/add")
def add():
    return render_template("pacientes_add.html")


@bp_pacientes.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    if nome and idade:
        db_paciente = Paciente(nome, idade)
        db.session.add(db_paciente)
        db.session.commit()
        flash("Paciente cadastrado!")
        return redirect("/pacientes")
    else:
        flash("Preencha todos os campos!")
        return redirect("/pacientes/add")
    

@bp_pacientes.route("/remove/<int:id>")
def remove(id):
    p = Paciente.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Paciente removido!")
    except:
        flash("Paciente Inválido!")
    return redirect("/pacientes")


@bp_pacientes.route("/edit/<int:id>")
def edit(id):
    p = Paciente.query.get(id)
    return render_template("pacientes_edit.html", dados=p)


@bp_pacientes.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    id_paciente = request.form.get("id_paciente")
    if nome and idade and id_paciente:
        p = Paciente.query.get(id_paciente)
        p.nome = nome
        p.idade = idade
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/pacientes")