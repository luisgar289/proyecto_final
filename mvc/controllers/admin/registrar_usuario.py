import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token
import json

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Registrar_usuario: #pagin sign up
    def GET(self):
        cookie = web.cookies().get('localid') #obtiene la cookie localid
        all_users = db.child("usuarios").get() #obtiene todos los usuarios de la base de datos
        for user in all_users.each(): #recorre todos los usuarios
            usuario = user.key() #obtiene la llave del usuario
            level = user.val()['level'] #obtiene el nivel del usuario
            if (usuario == cookie and level == "admin"): #compara la llave con la cookie, si son iguales muestra la pagina bienvenida.html
                message = None
                return render.registrar_usuario(message) 
                break
        else: #si no son iguales, redirecciona a la pagina de login
            web.setcookie('localid', "None")
            return web.seeother('/login') #redireccion la pagina login.html


    def POST(self):
        try:
            #obtiene los datos del formulario
            message = None
            formulario = web.input()
            email = formulario.email
            password= formulario.password
            nombre = formulario.nombre
            telefono = formulario.telefono
            nivel = formulario.nivel
            estado = formulario.estado
            user = auth.create_user_with_email_and_password(email, password) #crea un nuevo usuario en firebase
            datos = {'nombre': nombre, 'telefono': telefono, 'email':email, 'level':nivel, 'status':estado} #crea un diccionario con los datos del usuario
            resultados = db.child("usuarios").child(user['localId']).set(datos) #guarda los datos en la base de datos
            return web.seeother('/usuarios') #redirecciona a la pagina del login
        except Exception as error: #recopila los datos del error
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error signup.POST: {}".format(message)) #imprime en la terminal el error
            return render.registrar_usuario(message) #muestra la pagina signup.html con el error
