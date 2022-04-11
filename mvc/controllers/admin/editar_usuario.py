

import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Editar_usuario:
    def GET(self, localId):
        user = db.child('usuarios').child(localId).get() #obtiene todos los usuarios de la base de datos
        return render.editar_usuario(user)
    def POST(self, localId):
        try:
            #obtiene los datos del formulario
            formulario = web.input()
            id = formulario.id
            email = formulario.email
            nombre = formulario.nombre
            telefono = formulario.telefono
            tipo = formulario.tipo
            datos = {'nombre': nombre, 'telefono': telefono, 'email':email, 'level':tipo} #crea un diccionario con los datos del usuario
            resultados = db.child("usuarios").child(id).update(datos) #guarda los datos en la base de datos
            return web.seeother('/usuarios') #redirecciona a la pagina de usuarios
        except Exception as error:
            print("Error actualizar_usuario.POST: {}".format(error)) #imprime en la terminal el error
            return web.seeother('/usuarios') #redirecciona a la pagina de usuarios