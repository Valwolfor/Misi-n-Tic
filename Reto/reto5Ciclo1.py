#Se necesita organizar una información por cierto criterios y tomando una muestra.

import pandas as pd

pd.options.display.max_rows=10  #Especificación para configurar pandas en un maximo de rows

#ruta file csv
rutaFileCsv = "https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv"

#función. 
def listaPeliculas(rutaFileCsv:str)->str :
    #Función para llamar archivo filtrando y contruir los elementos solicitados.
    try:
        datosCsv = pd.read_csv(rutaFileCsv, sep = ',')
    except:
        print("Error al leer el archivo de datos.")
    tablaResultado = pd.DataFrame(data = datosCsv, columns = ["Country", "Languages", "Gross Earnings"])
    tablaResultado.to_csv("tablaResultado", sep = ',')
    tablaResultado = pd.read_csv(rutaFileCsv, sep = ',')
    
    print(tablaResultado)

listaPeliculas(rutaFileCsv)
print(listaPeliculas)