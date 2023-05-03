from geral.config import *

class Pessoa(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)
    curso = db.Column(db.Text)
    cpf = db.Column(db.Text)

    
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone + ", " + self.curso + ", " + self.cpf 
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "curso": self.curso,
            "cpf": self.cpf
        }

