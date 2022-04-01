import app
import web
import mvc.controllers.public.firebase_config as token
import pyrebase

render = web.template.render('mvc/views/public/') #configura la ubicacion de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Suspend:
    def GET(self):
        users = db.child("usuarios").get()
        return render.suspend(users) #muestra la pagina suspend.html