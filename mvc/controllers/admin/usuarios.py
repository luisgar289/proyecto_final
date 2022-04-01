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
            users = db.child("usuarios").get() #obtiene todos los usuarios de la base de datos
            return render.usuarios(users) #muestra la pagina usuarios.html
        except Exception as error:
            print("Error usuarios.GET: {}".format(error))
            return render.usuarios(error)