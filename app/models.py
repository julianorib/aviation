from app import db

class Aviao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    prefixo = db.Column(db.String(20), nullable=False)
    foto_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Aviao {self.nome}>"
