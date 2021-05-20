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
    print("Opcion 2: Crear un document al bucket en blanc")
    print("Opcion 3: Penjar un document al bucket")
    print("Opcion 4: Eliminar document csv al bucket")
    print("Opcion 5: Afegir una nova dada a un document csv")
    print("Opcion 6: Realitzar una consulta document")
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
            infor = info + ", " + input()
            print("Introudeix organica:")
            infor = info + ", " + input()
            print("Introudeix el programa:")
            infor = info + ", " + input()
            print("Introudeix economica:")
            infor = info + ", " + input()
            print("Introudeix descripcio de la partida:")
            infor = info + ", " + input()
            print("Introudeix els credits inicials:")
            infor = info + ", " + input()
            print("Introudeix la modificacio de credits:")
            infor = info + ", " + input()
            print("Introudeix els credits totals consignats:")
            infor = info + ", " + input()
            print("Introudeix les disposicions o compromisos")
            infor = info + ", " + input()
            print("Introudeix les obligacions:")
            infor = info + ", " + input()

        if opcion == 6: 
            print("\nDe quin any vols consultar les dades? ")
            any = int(input())
        
        opcion = mostrarMenu()