import re
import lithops
from lithops import Storage
import pandas as pd
from io import StringIO

def map_tables(params):
    storage = Storage()
    if params[0] == 'JOIN':
        s=str(params[1],'latin-1')
        data = StringIO(s) 
        economiaDF=pd.read_csv(data,header=0,delimiter=';')
        s=str(params[2],'latin-1')
        data = StringIO(s) 
        demografiaDF=pd.read_csv(data,header=0,delimiter=';')
        economiaPerDensitat = economiaDF.set_index(params[3]).join(demografiaDF.set_index(params[3]))
        economiaPerDensitat=economiaPerDensitat[[params[4],params[5]]]
        economiaPerDensitat.to_csv('./' + params[6] + '.csv')
        f = open(params[6] +".csv", "r")
        text = f.read()
        Storage.put_object(storage,'2021sdvictor',params[6] + '.csv',text)
        return params[6]
    if params[0] == 'SELECT':
        if params[4] == 'evolucioCovidEducatiuPositius':
            csv = storage.get_object('2021sdvictor', '7_evolucio_covid_educatiu.csv')
            s=str(csv,'UTF-8')
            data = StringIO(s) 
            df=pd.read_csv(data,header=0,delimiter=';',nrows=50000)
            result = df.loc[df[params[2]] > params[3]]
            result = result[["DATA","CODI_CENTRE","ALUMNES_POSITIUS_ACUM"]]
        else:
            csv = storage.get_object('2021sdvictor', '1_evolucio_covid.csv')
            s=str(csv,'latin-1')
            data = StringIO(s) 
            df=pd.read_csv(data,header=0,delimiter=';')
            result = df.loc[df[params[2]] == params[3]]
            result = result[["COMARCA","DATA","POSITIUS"]]
        result.to_csv('./' + params[4] + '.csv')
        f = open(params[4] +".csv", "r")
        text = f.read()
        Storage.put_object(storage,'2021sdvictor',params[4] + '.csv',text)
        return params[4]

if __name__ == '__main__':
    #STAGE 2: DATA PROCESSING
    storage = Storage()
    evolucio_covid = storage.get_object('2021sdvictor', '1_evolucio_covid.csv')
    demografia = storage.get_object('2021sdvictor', '2_demografia.csv')
    territori_ambiental = storage.get_object('2021sdvictor', '3_territori_ambiental.csv')
    infraestructura_sanitaria = storage.get_object('2021sdvictor', '4_infraestructura_sanitaria.csv')
    economia = storage.get_object('2021sdvictor', '5_economia.csv')
    infraestructura_educativa = storage.get_object('2021sdvictor', '6_infraestructura_educativa.csv')
    evolucio_covid_educatiu = storage.get_object('2021sdvictor', '7_evolucio_covid_educatiu.csv')
    #iterdata s'ha de definir com una llista de llistats amb parametres.
    #Aquest parametres son els seguents per als JOINS:
    #0: tipus d'operació (join o select)
    #1: csv de la taula 1 de la que volem fer join
    #2: csv de la taula 2 a la que volem fer join
    #3: nom de la taula que tenen en comú per a fer el join
    #4: columna de la taula 1 que volem que surti al nou csv
    #5: columna de la taula 2 que volem que surti al nou csv
    #6: nom del nou csv

    #Parametres pels selects:
    #0: tipus d'operació (join o select)
    #1: csv de la taula 1 de la que volem fer el select
    #2: columna que volem comparar
    #3: valor amb el que comparar la columna
    #4: nom del nou csv
    iterdata = [
        ['JOIN',economia,demografia,'COMARCA','PIB_CAPITA','DENSITAT','densitatPerPIB'],
        ['JOIN',economia,infraestructura_sanitaria,'COMARCA','PIB_CAPITA','LLITS_1000_HAB','llitsPerPIB'],
        ['JOIN',territori_ambiental,demografia,'COMARCA','TIPUS_COMARCA','HABITANTS','habitantsPerTipusComarca'],
        ['SELECT','1_evolucio_covid','GRUP_EDAT','Entre 15 i 64','positiusEntre15i64Anys'],
        ['SELECT','7_evolucio_covid_educatiu','ALUMNES_POSITIUS_ACUM',0,'evolucioCovidEducatiuPositius']
    ]
    fexec = lithops.FunctionExecutor()
    fexec.map(map_tables, iterdata)
    print(fexec.get_result())
    
    