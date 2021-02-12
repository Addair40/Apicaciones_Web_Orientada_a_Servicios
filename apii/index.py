import web
import requests
import json

render = web.template.render("apii/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self):
    form = web.input()
    name = form["name"]

    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+name)
        
    name = result.json()
        
    items = name["items"]
        
    encoded = json.dumps(items)
    decoded = json.loads(encoded)


    url_1=str(decoded[0]["url_details"])
    imagen_1=str(decoded[0]["thumbnail"])
    paginas_1=str(decoded[0]["pages"])


    url="<label>'"+url_1+"'</label"
    imagen="<label>'"+imagen_1+"'</label"
    pagina="<label>'"+pagina_1+"'</label"

    datos={

      "url":"URL DEL LIBRO: "+url,
      "imagen":"IMAGEN: "+imagen,
      "pagina":"PAGINA: "+pagina
    }
    return render.index(datos)