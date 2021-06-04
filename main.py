from lithops import FunctionExecutor
from lithops import Storage
import matplotlib.pyplot as plt
import pandas as pd
import io
import requests
from requests.auth import HTTPBasicAuth
import requests
import json

BUCKET = '2020sd'

#IBM Cloud
config = {'lithops' : {'storage_bucket' : BUCKET},

          'ibm_cf':  {'endpoint': 'https://s3.eu-de.cloud-object-storage.appdomain.cloud',
                      'namespace': 'guillem.gorgori@estudiants.urv.cat_dev',
                      'api_key': 'hUKJ-4H0JyETfezS8XpZVEy8p6-BYhCsyPO8K8i_FVE9'},

          'ibm_cos': {'region': 'eu-de',
                      'api_key': 'hUKJ-4H0JyETfezS8XpZVEy8p6-BYhCsyPO8K8i_FVE9'}}

def mostrarMenu():
    print("Quina opcio vols fer?")
    print("Opcion 0: Sortir")
    print("Opcion 1: Llistar documents bucket")
    print("Opcion 2: Crear un document al bucket en blanc")
    print("Opcion 3: Penjar un document al bucket")
    print("Opcion 4: Eliminar document csv al bucket")
    print("Opcion 5: Afegir una nova dada a un document csv")
    print("Opcion 6: Realitzar una consulta document")
    print("Opcion 7: Invocar funcion IBM cloud")
    print("Opcion 8: Genera el gráfico que quieras")
    print("Opción 9: Genera el gráfico de ejemplo de 'PAGAMENTS REALITZATS' per 'Alcaldia-Òrgans de govern-Dietes organs govern'")
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
    
if __name__ == '__main__':
    inicialitzar()
    storage = Storage(config=config)
    opcion = mostrarMenu()
    while(opcion != 0):
        if opcion == 1: 
            llistarArxiusBucket()
        
        if opcion == 2: 
            print("\nQuin nom vols que tingui el document nou al bucket? ")
            fitxer = input()
            obj_id = storage.put_cloudobject('', BUCKET, fitxer)
        
        if opcion == 3: 
            print("\nQuin document vols penjar? ")
            fitxer = input()

            f = open(fitxer, 'rb')
            obj_id = storage.put_cloudobject(io.BytesIO(f.read()), BUCKET, fitxer)

        if opcion == 4: 
            llistarArxiusBucket()
            print("\nQuin document vols eliminar? ")
            fitxer = input()
            storage.delete_object(BUCKET, fitxer)

        if opcion == 5: 
            llistarArxiusBucket()
            print("\nA quin fitxer vols introduir noves dades? ")
            fitxer = input()

            print("Introudeix l\'id:")
            info = input()
            print("Introudeix l\'any:")
            info = info + ", " + input()
            print("Introudeix organica:")
            info = info + ", " + input()
            print("Introudeix el programa:")
            info = info + ", " + input()
            print("Introudeix economica:")
            info = info + ", " + input()
            print("Introudeix descripcio de la partida:")
            info = info + ", " + input()
            print("Introudeix els credits inicials:")
            info = info + ", " + input()
            print("Introudeix la modificacio de credits:")
            info = info + ", " + input()
            print("Introudeix els credits totals consignats:")
            info = info + ", " + input()
            print("Introudeix les disposicions o compromisos")
            info = info + ", " + input()
            print("Introudeix les obligacions:")
            info = info + ", " + input()

            contingut=storage.get_object(bucket=BUCKET, key=fitxer)
            contingut=contingut.decode()

            contingut = contingut + "\n" + info

            obj_id = storage.put_cloudobject(contingut, BUCKET, fitxer)

        if opcion == 6: 
            print("\nDe quin any vols consultar les dades? ")
            any = int(input())

        if opcion == 7: 
            response = json.loads(requests.get("https://eu-gb.functions.appdomain.cloud/api/v1/web/guillem.gorgori%40estudiants.urv.cat_dev/SD/hello.json").text)
            print("\n")
            print(response)
            print("\n")
        if opcion == 8:
            print("Introdueix el nom de la columna a analitzar (per exemple 'PAGAMENTS REALITZATS')")
            col = input()
            print("Introdueix un valor de alguna fila de 'DESCRIPCIO PARTIDA' per a analitzar")
            row = input()
            values = { 
                "valorAConsultar": col, #valor que volem analitzar graficament
                "columnaACercar": "DESCRIPCIÓ PARTIDA" , #columna de la que volem buscar el id
                "idCerca": row #valor del csv del que volem extreure dades
            }
            r = getCsvData(values)
            plt.figure()
            plt.plot(r["anys"], r["consultes"])
            plt.xlabel(values["valorAConsultar"], fontsize=18)
            plt.ylabel('Anys', fontsize=16)
            plt.savefig("./images/" + col + "Reus.png")
            print("Gràfic generat a ./images")
            print()
        if opcion == 9:
            values = { 
                "valorAConsultar": "PAGAMENTS REALITZATS", #valor que volem analitzar graficament
                "columnaACercar": "DESCRIPCIÓ PARTIDA" , #columna de la que volem buscar el id
                "idCerca": "Alcaldia-Òrgans de govern-Dietes organs govern" #valor del csv del que volem extreure dades
            }
            r = getCsvData(values)
            plt.figure()
            plt.plot(r["anys"], r["consultes"])
            plt.xlabel(values["valorAConsultar"], fontsize=18)
            plt.ylabel('Anys', fontsize=16)
            plt.savefig("./images/DespesesReus.png")
            print("Gràfic generat a ./images")
            print()
        opcion = mostrarMenu()