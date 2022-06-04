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
            datosCsv = pd.read_csv(rutaFileCsv, sep = ',', usecols = ["Country", "Language", "Gross Earnings"])
            tablaGanancias = pd.pivot_table(datosCsv, index = ["Country", "Language"])
            return tablaGanancias.head(10)
        except:
            return f"Error al leer el archivo de datos."
    else:
        return f"Extensión inválida."
    
#Llamado de la función con impresión, esta vaina no deja pasar si no es print.
print(listaPeliculas(rutaFileCsv))
