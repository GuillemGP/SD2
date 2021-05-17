def mostrarMenu():
    print("Quina opcio vols fer?")
    print("Opcion 0: Sortir")
    print("Opcion 1: Llistar documents bucket")
    print("Opcion 2: Afegir document csv al bucket")
    print("Opcion 3: Eliminar document csv al bucket")
    print("Opcion 4: Afegir dada a un document csv")
    print("Opcion 45: Realitzar consulta document")
    opcion = int(input())
    return opcion

print('Practica 2 SD\n')

opcion = mostrarMenu()
while(opcion != 0):
    if opcion == 1: 
        print("Opcio 1: ")
        
    if opcion == 2: 
        print("Opcio 2: ")
    
    if opcion == 3: 
        print("Opcio 3: ")

    if opcion == 4: 
        print("Opcio 4: ")
    
    if opcion == 5: 
        print("Opcio 5: ")