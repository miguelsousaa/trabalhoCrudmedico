from database import db


class Paciente(db.Model):
    __tablename__ = 'paciente'
    id_paciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

    def __repr__(self):
        return f"<Paciente {self.nome}>"
    

class Consulta(db.Model):
    __tablename__ = 'consulta'
    id_consulta = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    observacoes = db.Column(db.String(255))
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))

    paciente = db.relationship('Paciente', foreign_keys=id_paciente)


    def __init__(self, data, observacoes, id_paciente):
        self.data = data
        self.observacoes = observacoes
        self.id_paciente = id_paciente

    
    def __repr__(self):
        return f"<Consulta {self.data} - {self.paciente.nome}>"