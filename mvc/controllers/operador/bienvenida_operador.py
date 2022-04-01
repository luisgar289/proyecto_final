import app
import web

render = web.template.render("mvc/views/operador/")

class Bienvenida_operador:
    def GET(self):
        nombre = None
        return render.bienvenida_operador()