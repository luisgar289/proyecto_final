import app
import web
import pyrebase
import mvc.controllers.public.firebase_config as token

render = web.template.render("mvc/views/operador/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Bienvenida_operador:
    def GET(self):
        cookie = web.cookies().get('localid') #obtiene la cookie localid
        all_users = db.child("usuarios").get() #obtiene todos los usuarios
        nombre = db.child("usuarios").child(cookie).get()
        estado_s1 = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        estado_s2 = db.child("sensores").child("sucursal2").child("enfriamiento").get()
        temperatura_s1 = db.child("sensores").child("sucursal1").child("temperatura").get()
        temperatura_s2 = db.child("sensores").child("sucursal2").child("temperatura").get()
        return render.bienvenida_operador(estado_s1, estado_s2, nombre, temperatura_s1, temperatura_s2)
    
    def POST(self):
        form = web.input()
        s1 = form.enfriamiento_s1
        s2 = form.enfriamiento_s2
        db.child("sensores").child("sucursal1").update({"enfriamiento": s1})
        db.child("sensores").child("sucursal2").update({"enfriamiento": s2})
        cookie = web.cookies().get('localid')
        nombre = db.child("usuarios").child(cookie).get()
        estado_s1 = db.child("sensores").child("sucursal1").child("enfriamiento").get()
        estado_s2 = db.child("sensores").child("sucursal2").child("enfriamiento").get()
        temperatura_s1 = db.child("sensores").child("sucursal1").child("temperatura").get()
        temperatura_s2 = db.child("sensores").child("sucursal2").child("temperatura").get()
        return render.bienvenida_operador(estado_s1, estado_s2, nombre, temperatura_s1, temperatura_s2)