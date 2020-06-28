# ORM: Object Relational Map
from flask import Flask, request, Response
from flask import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class ToJson():
    def to_json(self):
        return json.dumps({col.name: getattr(self, col.name) for col in self.__table__.columns })


class Usuarios(Base, ToJson):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    usuario = Column(String)
    password = Column(String)
    mail = Column(String)
    peso = Column(Integer)
    altura = Column(Integer)
    menu = Column(String)
    
class TipoMenu(Base, ToJson):
    __tablename__ = 'tipomenu'
    id = Column(Integer, primary_key=True)
    tipoMenu= Column(String)

class Categoria(Base, ToJson):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    descripcion= Column(String)

class Comidas(Base, ToJson):
    __tablename__ = 'comidas'
    id = Column(Integer, primary_key=True)
    descripcion= Column(String)
    idcategoria= Column(Integer, ForeignKey('categoria.id'))
    categoria= relationship(
        Categoria,
        backref=backref('categoria',uselist=True,cascade='delete,all')
    )
    porcion= Column(Integer)
    calorias= Column(Integer)
    idtipomenu= Column(Integer, ForeignKey('tipomenu.id'))
    tipomenu= relationship(
        TipoMenu,
        backref=backref('comidas',uselist=True,cascade='delete,all')
    )
    idusuario= Column(Integer, ForeignKey('usuarios.id'), default='')
    usuarios= relationship(
        Usuarios,
        backref=backref('usuarios',uselist=True,cascade='delete,all')
    )
    seleccionada= Column(Boolean, default=False)
    


engine = create_engine('sqlite:///base_servido.sqlite')

session = sessionmaker()
session.configure(bind=engine)

app = Flask(__name__) 

@app.route('/crearbase')
def crear_base():
    Base.metadata.create_all(engine)
    usuarios = Usuarios(nombre='Prueba',apellido='base',usuario='Administrador',password='1234',mail='sarasa@mail.com',peso='59',altura='170')
    s = session()
    s.add(usuarios)
    s.commit()

    return 'Ok'

@app.route('/populateTipo')
def populateTipo():
    menu1 = TipoMenu(tipoMenu="Carnes y vegetales")
    s = session()
    s.add(menu1)
    s.commit()
    
    menu2 = TipoMenu(tipoMenu="Vegetariano")
    s.add(menu2)
    s.commit()
    
    menu3= TipoMenu(tipoMenu="Vegano")
    s.add(menu3)
    s.commit()
    
    return 'Ok'


@app.route('/populateComidas')
def populateComidas():
    menu = Comidas(descripcion='1 te, 3 tostadas, mermelada light',idcategoria='1', calorias='75', idtipomenu='1')
    s = session()
    s.add(menu)
    s.commit()
    
    menu = Comidas(descripcion='1 churrasco, 1 rebanada de pan, ensalada lechuga-tomate',idcategoria='2', calorias='500', idtipomenu='1')
    s.add(menu)
    s.commit()
    
    menu = Comidas(descripcion='Cafe con leche, 4 galletitas de agua, mermelada y queso',idcategoria='3', calorias='133', idtipomenu='1')
    s.add(menu)
    s.commit()
    
    menu = Comidas(descripcion='Pechuga de pollo, rebanada de pan, ensalada mixta',idcategoria='4', calorias='450', idtipomenu='1')
    s.add(menu)
    s.commit()
    
    return 'Ok'

@app.route('/populateCategorias')
def populateCategorias():
    menu1 = Categoria(descripcion='Desayuno')
    s = session()
    s.add(menu1)
    s.commit()
    
    menu2 = Categoria(descripcion='Almuerzo')
    s = session()
    s.add(menu2)
    s.commit()
    
    menu3 = Categoria(descripcion='Merienda')
    s = session()
    s.add(menu3)
    s.commit()
    
    menu4 = Categoria(descripcion='Cena')
    s = session()
    s.add(menu4)
    s.commit()
    
    return 'Ok'

@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    if not 'username' in request.form:
        return Response("Nombre de usuario no especificado", status=400)

    if not 'password' in request.form:
        return Response("Contraseña no especificada", status=400)

    username = request.form['username']
    password = request.form['password']

    s = session()
    d = s.query(Usuarios).filter(Usuarios.usuario==username).first()
    if d.password != password:
        return Response("Usuario/Contraseña incorrecto", status=400)
    
    return Response('{"token":"esteesuntoken1234"}', status=201, mimetype='application/json')




# @app.route('/departamento', methods=['POST'])
# def create_departamento():
#     if not 'nombre' in request.form:
#         return Response("Nombre no especificado", status=400)

#     nombre = request.form['nombre']
#     if nombre == '':
#         return Response("{'mensaje_error':'Nombre vacio'}", status=400, mimetype='application/json')

#     depto = Departamento(nombre=nombre)

#     # depto = Departamento()
#     # depto.nombre = nombre

#     s = session()
#     s.add(depto)
#     s.commit()

#     return Response(str(depto.id), status=201, mimetype='application/json')

# @app.route('/departamento/<int:id>')
# def get_departamento(id):
#     s = session()
#     d = s.query(Departamento).filter(Departamento.id==id).one()
    
#     return Response(d.to_json(), status=200, mimetype='application/json')

# @app.route('/departamento')
# def list_departamento():
#     s = session()
#     dptos = s.query(Departamento)
#     return Response(json.dumps([d.to_json() for d in dptos]), status=200, mimetype='application/json')

# @app.route('/departamento', methods=['PUT'])
# def put_departamento():
#     id = request.form['id']
#     nombre = request.form['nombre']
    
#     s = session()
#     d = s.query(Departamento).filter(Departamento.id==id).one()
#     d.nombre = nombre
#     s.commit()
    
#     return Response(status=204)


if __name__ == '__main__':
    app.run(port=9001)