#Se necesita organizar una información por cierto criterios y tomando una muestra.

from operator import index
import pandas as pd
pd.options.display.max_rows=10  #Especificación para configurar pandas en un maximo de rows

#ruta file csv
rutaFileCsv = "https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv"

#función. 
def listaPeliculas(rutaFileCsv:str)->str :
    #Función para llamar archivo filtrando y contruir los elementos solicitados.
    # try:
    datosCsv = pd.read_csv(rutaFileCsv, sep = ',',index_col = ["Country", "Language"], usecols = ["Country", "Language", "Gross Earnings"])
    # except:
    
    print(datosCsv)

listaPeliculas(rutaFileCsv)
print(listaPeliculas)