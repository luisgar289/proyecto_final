import web
import app

class Logout:
    def GET(self):
        web.setcookie('localid', "None") #establece la cookie en None
        return web.seeother('/login') #regresa a la pagina de login