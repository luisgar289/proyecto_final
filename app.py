import web
import pyrebase
import json 

urls = (
    '/', 'mvc.controllers.public.index.Index', #se indica la ruta donde esta el archivo .py
    '/login', 'mvc.controllers.public.login.Login', #ruta de login
    '/recuperar_contrasena','mvc.controllers.public.recuperar.Recuperar', #ruta de recuperar contraseña
    '/suspend', 'mvc.controllers.public.suspend.Suspend', #ruta para usuarios suspendidos
    '/logout', 'mvc.controllers.public.logout.Logout', #ruta para cerrar sesión
    '/bienvenida_operador', 'mvc.controllers.operador.bienvenida_operador.Bienvenida_operador', #ruta de bienvenida_operador
)
app = web.application(urls, globals())
wsgiapp = app.wsgifunc()

if __name__ == "__main__":
    app.run()