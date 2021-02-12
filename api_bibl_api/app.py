import requests
import json

result = requests.get("https://www.etnassoft.com/api/v1/get/?millona")


periodico = result.json()

items = periodico
#print(items)

encoded = json.dumps(items)
decoded = json.loads(encoded)

lib=str(decoded[0]["ID"])
print(lib)

url=str(decoded[0]["url_details"])
print(url)

imagen=str(decoded[0]["thumbnail"])
print(imagen)

pagina=str(decoded[0]["pages"])
print(pagina)