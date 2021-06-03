import requests
import json
from requests.auth import HTTPBasicAuth
url = 'https://us-south.functions.cloud.ibm.com/api/v1/namespaces/victor.cano%40estudiants.urv.cat_dev/actions/plolt?blocking=true'
data = { 
    "valorAConsultar": "PAGAMENTS REALITZATS",
    "columnaACercar": "DESCRIPCIÓ PARTIDA" , 
    "idCerca": "Alcaldia-Òrgans de govern-Dietes organs govern"
}
jsonData = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=jsonData, headers=headers, auth=HTTPBasicAuth('8aaf2c73-23b9-4c80-abf1-855bffabd931', '8jiLkY0XH3lWxRnKfnwyIW2xT9v7UJUrJRmtblBfwTUfr3jKLfR5CsoZn6KjLsxz'))
print(r.text)
response = json.loads(r.text)
print (response["response"]["result"]["anys"])
print (response["response"]["result"]["consultes"])