import web
import requests
import json

render = web.template.render("apis/")

class Index():

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()


        result = requests.get("https://repl.it/@Addair40/ApicacionesWebOrientadaaServicios#horoscopos/api.py)
        

