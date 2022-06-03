#Se necesita organizar una información por cierto criterios y tomando una muestra.

import pandas as pd

pd.options.display.max_rows=10  #Especificación para configurar pandas en un maximo de rows

#ruta file csv
rutaFileCsv = "https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv"

#función. 
def listaPeliculas(rutaFileCsv:str)->str :
    
    import numpy as np
    
    datosCsv = pd.read_csv(rutaFileCsv, sep = ',') #index_col = ["Country", "Languages", "Gross Earnings"]
    
    # tablaResultado = pd.DataFrame(data = datosCsv, columns = ["Country", "Languages", "Gross Earnings"])
    
    print(datosCsv)

listaPeliculas(rutaFileCsv)
print(listaPeliculas)