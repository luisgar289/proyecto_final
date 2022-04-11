from tracemalloc import stop
import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Usuarios:
    def GET(self):
        try:
            cookie = web.cookies().get('localid') #obtiene la cookie localid
            all_users = db.child("usuarios").get() #obtiene todos los usuarios
            for user in all_users.each(): #recorre todos los usuarios
                print(user.key())
                if user.key() == cookie and user.val()['level'] == "admin" : #compara la llave con la cookie, si son iguales muestra la pagina bienvenida.html
                    users = db.child("usuarios").get() #obtiene todos los usuarios de la base de datos
                    return render.usuarios(users)
                    break
            else: #si no son iguales, redirecciona a la pagina de login
                web.setcookie('localid', "None")
                return web.seeother('/login') #redireccion la pagina login.html
        except:
            return web.seeother('/login')
        
        