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
        desactivar = db.child('usuarios').child(localId).update({'status':'false'})
        return web.seeother('/usuarios')