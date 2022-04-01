import web
import pyrebase
import json 

urls = (
    '/', 'mvc.controllers.public.index.Index', #se indica la ruta donde esta el archivo .py
)
app = web.application(urls, globals())
wsgiapp = app.wsgifunc()

if __name__ == "__main__":
    app.run()