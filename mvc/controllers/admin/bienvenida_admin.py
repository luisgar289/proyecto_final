import app
import web

render = web.template.render("mvc/views/admin/")

class Bienvenida_admin:
    def GET(self):
        nombre = None
        return render.bienvenida_admin()