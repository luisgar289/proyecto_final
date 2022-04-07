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
        estado_s1 = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        estado_s2 = db.child("sensores").child("sucursal2").child("enfriamiento").get()
        return render.bienvenida_admin(estado_s1, estado_s2)

    def POST(self):
        form = web.input()
        s1 = form.enfriamiento_s1
        s2 = form.enfriamiento_s2
        db.child("sensores").child("sucursal1").update({"enfriamiento": s1})
        db.child("sensores").child("sucursal2").update({"enfriamiento": s2})
        estado_s1 = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        estado_s2 = db.child("sensores").child("sucursal2").child("enfriamiento").get()
        return render.bienvenida_admin(estado_s1, estado_s2)