import web
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

urls = (
    '/parametros?', 'Parametros'
)
app = web.application(urls, globals())

class Parametros:

    json_file = {}

    def GET(self):

        parametros = web.input()
        action = parametros.action

        if action == "get".replace(" ",""):
            return self.Leer()
        elif action == "put".replace(" ",""):
            Nombre = parametros.Nombre
            Nacimiento = parametros.Nacimiento
            return self.Ingresar(Nombre, Nacimiento)

    def Ingresar (self, nombre, nacimiento):
        try:
            fecha = datetime.strptime(nacimiento, "%d-%m-%Y")
            edad = relativedelta(datetime.now(), fecha_nacimiento)
            edad = (f"{edad.years} años.")
            persona = {}
            persona["nombre"] = nombre
            persona["fecha"] = nacimiento
            persona["edad"] = edad
            
            try:
                with open("static/datos.json") as file:
                    self.json_file = json.load(file)
                    self.json_file["personas"].append(persona)
                    with open("static/datos.json","w") as file:
                        json.dump(self.json_file, file)
                        data = {}
                        data["success"] = "DATOS CORRECTOS."
                        data["status"] = 200
                        return json.dumps(data)
            
        except:
            data = {}
            data["error"] = "ERROR DATOS NO ENCONTRADOS"
            data["status"] = 404
            return json.dumps(data)

    def Leer(self):
        with open("static/datos.json") as file:
            self.json_file = json.load(file)
            return json.dumps(self.json_file)

if __name__ == "__main__":
    app.run()