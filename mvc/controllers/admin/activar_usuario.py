import web
import app
import pyrebase
import mvc.controllers.public.firebase_config as token

render = web.template.render("mvc/views/admin/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Activar_usuario:
    def GET(self, localId):
        activar = db.child('usuarios').child(localId).update({'status':'true'})
        return web.seeother('/usuarios')
