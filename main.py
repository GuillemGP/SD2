from lithops import FunctionExecutor
from lithops import Storage

import io

BUCKET = '2020sd'

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
    print("Opcion 2: Afegir un document csv al bucket")
    print("Opcion 3: Eliminar document csv al bucket")
    print("Opcion 4: Afegir una nova dada a un document csv")
    print("Opcion 5: Realitzar una consulta document")
    opcion = int(input())
    return opcion

def my_function(obj_id, storage):
    print(obj_id)

    data = storage.get_cloudobject(obj_id)

    return data.decode()


print('Practica 2 SD\n')
print('Tractament de les dades pressupostaries de l\'ajuntament de Reus')
print('Les dades pressupostaries de cada any es guarden en un fitxer csv\n')

storage = Storage(config=config)

opcion = mostrarMenu()
while(opcion != 0):
    if opcion == 1: 
        print("Llista de fitxers guardats: ")
        print(storage.list_keys(BUCKET))
    
    if opcion == 2: 
        print("Quin document vols afegir? ")
        fitxer = input()

        f = open(fitxer, 'rb')
        obj_id = storage.put_cloudobject(io.BytesIO(f.read()), BUCKET, fitxer)

    if opcion == 3: 
        print("Quin document vols eliminar? ")
        fitxer = input()
        storage.delete_object('2020sd', fitxer)

    if opcion == 4: 
        print("De quin any vols introduir noves dades? ")
        any = int(input())

    if opcion == 5: 
        print("De quin any vols consultar les dades? ")
        any = int(input())
    
    opcion = mostrarMenu()