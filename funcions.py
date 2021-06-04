def mostrarMenu():
    print("Quina opcio vols fer?")
    print("Opcion 0: Sortir")
    print("Opcion 1: Llistar documents del nuvol")
    print("Opcion 2: Crear un document al nuvol en blanc")
    print("Opcion 3: Penjar un document al nuvol")
    print("Opcion 4: Eliminar document del nuvol")
    print("Opcion 5: Afegir una nova dada a un document csv")
    print("Opcion 6: Generar grafic")
    print("Opcion 7: Mostra per pantalla el contingut d'un fitxer del nuvol")
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