import web #se importa web.py
import mvc.controllers.public.firebase_config as token
import pyrebase
import app #se importa la variable app de app.py
import json

render = web.template.render("mvc/views/public/") #ruta de las vistas
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth() #verifica la conexión a firebase
db = firebase.database()

class Login: #pagina login
    def GET(self):
        message = None
        return render.login(message) #muestra la pagina login.html

    def POST(self):
        try:
            #obtiene los datos del formulario
            message = None
            formulario = web.input() 
            email = formulario.email 
            password= formulario.password
            #autentica los datos con firebase
            user = auth.sign_in_with_email_and_password(email, password)
            #obtiene los datos del usuario
            informacion = auth.get_account_info(user['idToken']) 
            localId = user['localId'] #obtiene el localId del usuario
            #genera una cookie
            web.setcookie('localid', localId)
            all_users = db.child("usuarios").get() #obtiene todos los usuarios
            for user in all_users.each():
                if user.key() == localId and user.val()['level'] == "admin": #compara el localId y el email
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida_admin') #redirecciona a la pagina de admin
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/suspend')
                elif user.key() == localId and user.val()['level'] == "operador":
                    if user.val()['status'] == 'true':
                        return web.seeother('/bienvenida_operador') #redirecciona a la pagina de operador
                    else:
                        admin = user.val()['level'] == "admin"
                        return web.seeother('/suspend')
        except Exception as error: #recopila y muestra los datos de algun error
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error login.POST: {}".format(message)) #imprime en la terminal el error
            return render.login(message) #muestra la pagina login.html con el error