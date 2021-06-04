import requests
import json

def mostrarMenu():
    print("Quina opcio vols fer?")
    print("Opcio 0: Sortir")
    print("Opcio 1: Llistar documents del nuvol")
    print("Opcio 2: Crear un document al nuvol en blanc")
    print("Opcio 3: Penjar un document al nuvol")
    print("Opcio 4: Eliminar document del nuvol")
    print("Opcio 5: Afegir una nova dada a un document csv")
    print("Opcio 6: Mostra per pantalla el contingut d'un fitxer del nuvol")
    print("Opcion 7: Genera el grafic que volguis")
    print("Opción 8: Genera el grafic d'exemple de 'PAGAMENTS REALITZATS' per 'Alcaldia-Òrgans de govern-Dietes organs govern'")
    opcion = int(input())
    return opcion

def llistarArxiusBucket():
    print("\nLlista de fitxers guardats al bucket: ")
    print(storage.list_keys(BUCKET))
    print("\n")

def inicialitzar():
    print('\n\nPractica 2 SD\n')
    print('Tractament de les dades pressupostaries de l\'ajuntament de Reus')
    print('Les dades pressupostaries de cada any es guarden en un fitxer csv\n')

def getCsvData(values):
    url = 'https://us-south.functions.cloud.ibm.com/api/v1/namespaces/victor.cano%40estudiants.urv.cat_dev/actions/plolt?blocking=true'
    data = { 
        "valorAConsultar": values["valorAConsultar"],
        "columnaACercar": "DESCRIPCIÓ PARTIDA" , 
        "idCerca": values["idCerca"]
    }
    jsonData = json.dumps(data)
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=jsonData, headers=headers, auth=HTTPBasicAuth('8aaf2c73-23b9-4c80-abf1-855bffabd931', '8jiLkY0XH3lWxRnKfnwyIW2xT9v7UJUrJRmtblBfwTUfr3jKLfR5CsoZn6KjLsxz'))
    print("S'ha rebut la resposta de la funcio del cloud")
    response = json.loads(r.text)
    result = {}
    result["anys"] = response["response"]["result"]["anys"]
    result["consultes"] = response["response"]["result"]["consultes"]
    return result