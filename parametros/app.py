import web
import json
urls = (
    '/edad?', 'Edad'
)
app = web.application(urls, globals())

class Edad:



    def GET(self):
        try:
            parametros = web.input() 
            nombre = parametros.nombre
            fech_dia = int(parametros.fech_dia)
            fech_mes = int(parametros.fech_mes)
            fech_ano = int(parametros.fech_ano) 
            

            edad = 2021 - fech_ano
            data = {}
            data["NOMBRE"] = nombre
            data["DIA"] = fech_dia
            data["MES"] = fech_mes
            data["ANO"] = fech_ano

            archivo = open("static/edad.txt","a")
            archivo.write("\n")
            archivo.write(str(data))
            archivo.close()
            return json.dumps(data)

        except:
            data = {}
            data["mensaje"] = "VERIFICA SUS DATOS POR FAVOR"
            return json.dumps(data)

if __name__ == "__main__":
    app.run()