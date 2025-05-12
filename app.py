from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Alunos
class Aluno(db.Model):
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=True)
 
# Criar o banco de dados e tabelas
with app.app_context():
    db.create_all()

# Rota para consultar todos os alunos
@app.route('/api/tabela alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    alunos_list = [{"nome": aluno.nome, "idade": aluno.idade} for aluno in alunos]
    return jsonify(alunos_list)


if __name__ == '__main__':
    app.run(debug=True)
