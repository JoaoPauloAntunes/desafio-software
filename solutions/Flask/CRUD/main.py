from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, request

e = create_engine('sqlite:///arquivo.db', echo=True)
Session = sessionmaker(bind=e)
Base = declarative_base(bind=e)
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200))
    
Base.metadata.create_all()

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def indice():
    s = Session()
    result = '<html>' # monta variavel com html a retornar
    if request.method == "POST":
        usuario = Usuario(nome=request.form["nome"])
        s.add(usuario)
        s.commit()
        result += '<p>Usuario incluido com sucesso!</p>'
    result += '<table><tr><th>ID</td><th>Nome</th></tr>' #cabecalho
    for usuario in s.query(Usuario):
        result += '<tr><td>{0.id}</td><td>{0.nome}</td></tr>'.format(usuario)
    result += '</table><form method="POST">Incluir novo usuario:'
    result += '<input name="nome" /><input type="submit"></form><html>'
    return result

if __name__ == '__main__':
    app.run()