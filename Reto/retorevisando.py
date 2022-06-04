#Se necesita organizar una información por cierto criterios y tomando una muestra.


import pandas as pd


#ruta file csv
rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

#función. 
def listaPeliculas(rutaFileCsv:str)->str :
    #Función para llamar archivo filtrando y contruir los elementos solicitados.
        
    #Creación de subconjunto y validación de archivo. 
    validador = rutaFileCsv.split(".")
    if "csv" in validador[-1]:
        
        try:
            datosCompletos = pd.read_csv(rutaFileCsv, sep = ',')
            datosCsv = pd.read_csv(rutaFileCsv, sep = ',', usecols = ["Country", "Language", "Gross Earnings"])
            subconjunto = datosCompletos["Country", "Language", "Gross Earnings"]
            print(subconjunto)
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")
    
    #convertirla en tabla dinamica. 
    # tablaDinamica = pd.pivot_table(datosCsv, index = ["Country", "Language"])
    #tomar solo 10 datos del total de la tabla. 
    # tablaDinamica = tablaDinamica.head(10) 
    
    # listaResultado = pd.unique(list(map(lambda x: x[0])))
    # print(datosCsv)
    # print(tablaDinamica)
    # print(listaResultado)

listaPeliculas(rutaFileCsv)

