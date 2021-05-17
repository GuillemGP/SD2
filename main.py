from lithops import FunctionExecutor
from lithops import Storage


def mostrarMenu():
    print("Quina opcio vols fer?")
    print("Opcion 0: Sortir")
    print("Opcion 1: Llistar documents bucket")
    print("Opcion 2: Afegir document csv al bucket")
    print("Opcion 3: Eliminar document csv al bucket")
    print("Opcion 4: Afegir dada a un document csv")
    print("Opcion 5: Realitzar consulta document")
    opcion = int(input())
    return opcion

print('Practica 2 SD\n')
print('Tractament de les dades pressupostaries de l\'ajuntament de Reus\n')
print('Les dades pressupostaries de cada any es guarden en un fitxer csv\n')



opcion = mostrarMenu()
while(opcion != 0):
    if opcion == 1: 
        print("Llista de fitxers guardats: ")
        
    if opcion == 2: 
        print("Quin document vol afegir? ")
        fitxer = input()
    
    if opcion == 3: 
        print("Quin document vol eliminar? ")
        fitxer = input()

    if opcion == 4: 
        print("De quin any vols introduir noves dades? ")
        any = int(input())
    
    if opcion == 5: 
        print("De quin any vols consultar les dades? ")
        any = int(input())