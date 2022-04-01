import web #se importa web.py
import app #e importa la variable app de app.py

render = web.template.render("mvc/views/public/") #ruta de las vistas

class Index: #clase Index
    def GET(self):
        return render.index()