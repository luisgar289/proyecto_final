import app
import web
import pyrebase
import mvc.controllers.public.firebase_config as token


render = web.template.render("mvc/views/admin/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Bienvenida_admin:
    def GET(self):
        estado = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        return render.bienvenida_admin(estado)

    def POST(self):
        form = web.input()
        enfriamiento = form.enfriamiento_s1
        db.child("sensores").child("sucursal1").update({"enfriamiento": enfriamiento})
        estado = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        return render.bienvenida_admin(estado)