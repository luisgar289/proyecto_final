import web #se importa web.py
import mvc.controllers.public.firebase_config as token
import pyrebase
import app #se importa la variable app de app.py
import json

render = web.template.render("mvc/views/public/")
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase

class Recuperar:
    def GET(self):
        message = None
        return render.recuperar(message)
    def POST(self):
        try:
            #obtiene los datos del formulario
            message = None
            formulario = web.input()
            email = formulario.email
            auth.send_password_reset_email(email) #enviá un correo de recuperación de contraseña
            return web.seeother('/login') #redirecciona a la pagina de login
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error recuperar.POST: {}".format(message))
            return render.recuperar(message)