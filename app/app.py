import os
import random
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import boto3
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configurações do AWS S3
s3_client = boto3.client('s3',
                         aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

# Modelo do Banco de Dados
class Aviao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    prefixo = db.Column(db.String(20), nullable=False)
    foto_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Aviao {self.nome}>"

# Rota da tela inicial
@app.route('/')
def index():
    aviões = Aviao.query.all()
    # Escolhe uma foto aleatória
    if aviões:
        aviao = random.choice(aviões)
        return render_template('index.html', aviao=aviao)
    return render_template('index.html', aviao=None)

# Rota para cadastro de avião
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        prefixo = request.form['prefixo']
        foto = request.files['foto']

        # Salva a foto no S3
        filename = secure_filename(foto.filename)
        s3_client.upload_fileobj(foto, os.getenv('AWS_BUCKET_NAME'), filename)
        foto_url = f"https://{os.getenv('AWS_BUCKET_NAME')}.s3.amazonaws.com/{filename}"

        # Salva os dados no MySQL
        novo_aviao = Aviao(nome=nome, prefixo=prefixo, foto_url=foto_url)
        db.session.add(novo_aviao)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')

# Rota para excluir avião
@app.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    aviao = Aviao.query.get(id)
    if aviao:
        # Exclui a foto do S3
        filename = aviao.foto_url.split('/')[-1]
        s3_client.delete_object(Bucket=os.getenv('AWS_BUCKET_NAME'), Key=filename)
        
        # Exclui o registro no banco de dados
        db.session.delete(aviao)
        db.session.commit()

    return redirect(url_for('index'))

# Rota para visualizar aviões cadastrados
@app.route('/visualizar')
def visualizar():
    aviões = Aviao.query.all()
    return render_template('view.html', aviões=aviões)

if __name__ == '__main__':
    app.run(debug=True)
