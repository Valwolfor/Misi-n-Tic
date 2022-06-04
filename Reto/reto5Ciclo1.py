#Se necesita organizar una información por cierto criterios y tomando una muestra.

import pandas as pd
pd.options.display.max_rows = 10  #Especificación para configurar pandas en un maximo de rows
#ruta file csv
rutaFileCsv = "https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv"

#función. 
def listaPeliculas(rutaFileCsv:str)->str :
    #Función para llamar archivo filtrando y contruir los elementos solicitados.
    # try:
    # datosCsv = pd.read_csv(rutaFileCsv, sep = ',', index_col = ["Country", "Language"], usecols = ["Country", "Language", "Gross Earnings"])
    datosCsvSC = pd.read_csv(rutaFileCsv, sep = ',', usecols = ["Country", "Language", "Gross Earnings"])
    # except:
        # print("Error al leer el archivo de datos.")
    tablaDinamica = pd.pivot_table(datosCsvSC, index = ["Country", "Language"], columns = "Gross Earnings")
    # tablaDinamica = pd.pivot_table(datosCsv)
    # print(datosCsvSC.head(10))
    # print(tablaDinamica)

listaPeliculas(rutaFileCsv)
print(listaPeliculas)