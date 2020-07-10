# ORM: Object Relational Map
from flask import Flask, request, Response
from flask import json, jsonify, make_response

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from werkzeug.security import generate_password_hash, check_password_hash

from random import randint


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
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
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
    
class ComidasUsuarios(Base, ToJson):
    __tablename__ = 'comidasusuarios'
    id = Column(Integer, primary_key=True)
    idUsuario= Column(Integer, ForeignKey('usuarios.id'))
    usuario= relationship(
        Usuarios,
        backref=backref('usuarios',uselist=True,cascade='delete,all')
    )
    idComida= Column(Integer, ForeignKey('comidas.id'))
    comida= relationship(
        Comidas,
        backref=backref('comidas',uselist=True,cascade='delete,all')
    )    


engine = create_engine('sqlite:///base_servido.sqlite')

session = sessionmaker()
session.configure(bind=engine)

app = Flask(__name__) 

@app.route('/crearbase')
def crear_base():
    Base.metadata.create_all(engine)
    #set_password('1234')
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

@app.route('/populateComidasUsuarios')
def populateComidasUsuarios():
    opcion1 = ComidasUsuarios(idUsuario='1',idComida='1')
    s = session()
    s.add(opcion1)
    s.commit()
    
    opcion2 = ComidasUsuarios(idUsuario='1', idComida='2')
    s = session()
    s.add(opcion2)
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
    if not 'username' in request.form:
        return Response("Nombre de usuario no especificado", status=400)

    if not 'password' in request.form:
        return Response("Contraseña no especificada", status=400)

    username = request.form['username']
    password = request.form['password']

    s = session()
   
    try:
        d = s.query(Usuarios).filter(Usuarios.usuario==username).first()
        if not d.check_password(password) or d.usuario != username:
            return Response("Usuario/Contraseña incorrecto", status=400)
    except(Exception):
        return Response("Cliente no registrado", status=404)   
    
    rand = randint(100000,999999)
    token = 'bearer'+str(rand)
    res_body = {"id":d.id,"token":token}
    res = make_response(res_body, 200)
    return res

@app.route('/register', methods=['POST'])
def create_usuario():
    if not 'nombre' in request.form:
        return Response("Nombre no especificado", status=400)
    if not 'apellido' in request.form:
        return Response("Apellido no especificado", status=400)
    if not 'usuario' in request.form:
        return Response("Usuario no especificado", status=400)
    if not 'password' in request.form:
        return Response("Contraseña no especificada", status=400)
    if not 'mail' in request.form:
        return Response("Mail no especificado", status=400)
    if not 'peso' in request.form:
        return Response("Peso no especificado", status=400)
    if not 'altura' in request.form:
        return Response("Altura no especificada", status=400)

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    user = request.form['usuario']
    password = request.form['password']
    mail = request.form['mail']
    peso = request.form['peso']
    altura = request.form['altura']
    menu = request.form['menu']


    s = session()
  
    us = s.query(Usuarios).get(user)
    if us is not None:
        return Response(text="El usuario ya existe", status=400)
    else:
        tMenu = s.query(TipoMenu).filter(TipoMenu.tipoMenu == menu).first()
        usuario = Usuarios(nombre=nombre,apellido=apellido,usuario=user,mail=mail,peso=peso,altura=altura, menu=tMenu.id)
        usuario.set_password(password)
        s.add(usuario)
        s.commit()
        return Response(str(usuario.id), status=201, mimetype='application/json')
            


@app.route('/opciones', methods=['GET'])
def buscar_opciones():
    s = session()
    comidas = s.query(Comidas)

    return Response(json.dumps([c.to_json() for c in comidas]), status=200, mimetype='application/json')

@app.route('/getUser')
def buscar_cliente():
    id = request.args.get('idUsuario')
    
    s = session()
    
    try:
        user = s.query(Usuarios).get(id)
        if user is not None:
            res_body = {
                "nombre": user.nombre,
                "apellido": user.apellido,
                "user": user.usuario,
                "password": user.password,
                "mail": user.mail,
                "peso": user.peso,
                "altura": user.altura,
                "menu": user.menu
            }
            res = make_response(res_body,200)
            return res
        else:
            return Response("Error al validar los datos", status=400)   
    except(Exception):
        return Response("Internal server error", status=500)
    

if __name__ == '__main__':
    app.run(port=9001)