import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Suspender_usuario:
    def GET(self, localId):
        cookie = web.cookies().get('localid') #obtiene la cookie localid
        all_users = db.child("usuarios").get() #obtiene todos los usuarios de la base de datos
        for user in all_users.each(): #recorre todos los usuarios
            usuario = user.key() #obtiene la llave del usuario
            level = user.val()['level'] #obtiene el nivel del usuario
            if (usuario == cookie and level == "admin"): #compara la llave con la cookie, si son iguales muestra la pagina bienvenida.html
                desactivar = db.child('usuarios').child(localId).update({'status':'false'})
                return web.seeother('/usuarios')
                break
        else: #si no son iguales, redirecciona a la pagina de login
            web.setcookie('localid', "None")
            return web.seeother('/login') #redireccion la pagina login.html