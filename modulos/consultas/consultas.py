from flask import Blueprint, render_template, request, redirect, flash
from models import Consulta, Paciente
from database import db

bp_consultas = Blueprint('consultas', __name__, template_folder="templates")

@bp_consultas.route("/")
def index():
    c = Consulta.query.all()
    return render_template("consultas.html", dados=c)


@bp_consultas.route("/add")
def add():
    c = Consulta.query.all()
    p = Paciente.query.all()
    return render_template("consultas_add.html", dados=c, pacientes=p)


@bp_consultas.route("/save", methods=['POST'])
def save():
    data = request.form.get("data")
    observacoes = request.form.get("observacoes")
    id_paciente = request.form.get("id_paciente")

    paciente = Paciente.query.all()

    if data and observacoes and id_paciente:
        db_consulta = Consulta(data, observacoes, id_paciente)
        db.session.add(db_consulta)
        db.session.commit()
        flash("Consulta cadastrada!")
        return redirect("/consultas")
    else:
        flash("Preencha todos os campos!")
        return redirect("/consultas/add")
    

@bp_consultas.route("/remove/<int:id>")
def remove(id):
    c = Consulta.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Consulta removida!")
    except:
        flash("Consulta Inválida!")
    return redirect("/consultas")


@bp_consultas.route("/edit/<int:id>")
def edit(id):
    c = Consulta.query.get(id)
    p = Paciente.query.all()
    return render_template("consultas_edit.html", dados=c, pacientes=p)


@bp_consultas.route("/edit-save", methods=['POST'])
def edit_save():
    data = request.form.get("data")
    observacoes = request.form.get("observacoes")
    id_paciente = request.form.get("id_paciente")
    id_consulta = request.form.get("id_consulta")
    if data and observacoes and id_paciente and id_consulta:
        c = Consulta.query.get(id_consulta)
        c.data = data
        c.observacoes = observacoes
        c.id_paciente = id_paciente
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/consultas")