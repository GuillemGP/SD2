from lithops import FunctionExecutor
from lithops import Storage
import matplotlib.pyplot as plt
import pandas as pd
import io

import funcions
import configIBMCloud
    
if __name__ == '__main__':
    funcions.inicialitzar()
    storage = Storage(config=configIBMCloud.config)
    opcion = funcions.mostrarMenu()
    while(opcion != 0):
        if opcion == 1: 
            funcions.llistarArxiusBucket()
        
        if opcion == 2: 
            print("\nQuin nom vols que tingui el document nou al bucket? ")
            fitxer = input()
            obj_id = storage.put_cloudobject('', configIBMCloud.BUCKET, fitxer)
        
        if opcion == 3: 
            print("\nQuin document vols penjar? ")
            fitxer = input()

            f = open(fitxer, 'rb')
            obj_id = storage.put_cloudobject(io.BytesIO(f.read()), configIBMCloud.BUCKET, fitxer)

        if opcion == 4: 
            funcions.llistarArxiusBucket()
            print("\nQuin document vols eliminar? ")
            fitxer = input()
            storage.delete_object(configIBMCloud.BUCKET, fitxer)

        if opcion == 5: 
            funcions.llistarArxiusBucket()
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

            contingut=storage.get_object(bucket=configIBMCloud.BUCKET, key=fitxer)
            contingut=contingut.decode()

            contingut = contingut + "\n" + info

            obj_id = storage.put_cloudobject(contingut, configIBMCloud.BUCKET, fitxer)
        
        if opcion == 6:
            funcions.llistarArxiusBucket()
            print("\nQuin fitxer vols mostrar per pantalla? ")
            fitxer = input()
            contingut=storage.get_object(bucket=configIBMCloud.BUCKET, key=fitxer)
            contingut=contingut.decode()
            print("\nContingut del fitxer:\n" + contingut + "\n")
        
        if opcion == 7:
            print("Introdueix el nom de la columna a analitzar (per exemple 'PAGAMENTS REALITZATS')")
            col = input()
            print("Introdueix un valor de alguna fila de 'DESCRIPCIO PARTIDA' per a analitzar")
            row = input()
            values = { 
                "valorAConsultar": col, #valor que volem analitzar graficament
                "columnaACercar": "DESCRIPCIÓ PARTIDA" , #columna de la que volem buscar el id
                "idCerca": row #valor del csv del que volem extreure dades
            }
            r = funcions.getCsvData(values)
            plt.figure()
            plt.plot(r["anys"], r["consultes"])
            plt.xlabel('Anys', fontsize=18)
            plt.ylabel(values["valorAConsultar"], fontsize=16)
            plt.savefig("./images/" + col + "Reus.png")                       #Si es un windows usar este formato
            #plt.savefig("/Users/guillemgorgoriperez/Desktop/DespesesReus.png") #Si es un macos usar este formato
            print("Gràfic generat a ./images")
            print()

        if opcion == 8:
            values = { 
                "valorAConsultar": "PAGAMENTS REALITZATS", #valor que volem analitzar graficament
                "columnaACercar": "DESCRIPCIÓ PARTIDA" , #columna de la que volem buscar el id
                "idCerca": "Alcaldia-Òrgans de govern-Dietes organs govern" #valor del csv del que volem extreure dades
            }
            r = funcions.getCsvData(values)
            plt.figure()
            plt.plot(r["anys"], r["consultes"])
            plt.xlabel('Anys', fontsize=18)
            plt.ylabel(values["valorAConsultar"], fontsize=16)
            plt.savefig("./images/DespesesReus.png")                          #Si es un windows usar este formato
            #plt.savefig("/Users/guillemgorgoriperez/Desktop/DespesesReus.png") #Si es un macos usar este formato
            print("Gràfic generat a ./images")
            print()
        
        opcion = funcions.mostrarMenu()