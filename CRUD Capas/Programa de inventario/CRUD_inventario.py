#Librería con la lógica de las operaciones CRUD
###############################################

#Para poder utilizar el archivo json que es el que tiene los datos. 
import json

#Adición de una tarea (Create). |Producto: tipo de producto, identificador a darle, y nombre. 
def Create(producto, identificador, productoNuevo):    
    producto[identificador] = productoNuevo #Mutación del diccionario por referencia      

#Consultar la información de todas las tareas (Read)
def Read(rutaArchivo='listadoProductos.json'):

    #Cargar el listado de tareas a un diccionario desde la capa de datos (archivo JSON)    
    diccionarioProductos = {}#Contenedor del listado de tareas que gestiona la App
    try:    
        with open(rutaArchivo) as archivo: 
            diccionarioProductos = json.load(archivo)
    except:
        print("No se pudo cargar la información de la capa de datos del primer cargue del json")
        return False #Reportar fallo en la carga

    #Retornar el contenedor o colección obtenido
    return diccionarioProductos

#Actualizar una tarea específica (Update)
def Update(producto, identificador, tareaActualizada):
    #Revisar los campos que llegan con información para actualizar
    for id_campo, campo in tareaActualizada.items():        
        if campo:
            producto[identificador][id_campo] = campo #Actualizar el campo del diccionario (referencia)

#Eliminar una tarea específica (Delete)
def Delete(producto, identificador):
    producto.pop(identificador)


#Operación de escritura en la capa de datos al cierre de la aplicación

def Write(producto, rutaArchivo='listadoProductos.json'):
    #Descargar contenedor de datos con las modificaciones realizadas por la App
    try:
        with open(rutaArchivo, 'w') as archivo_json:
            json.dump(producto, archivo_json)
    except:
        print("Error: No se pudo guardar la información en la capa de datos.")
        return False
    #Convertirlo en excel
    import pandas as pd
    try:
        pd.read_json(archivo_json).to_excel('data.xlsx', index=False)
    except:
        print("Error: No se pudo guardar la información en el archivo excel.")
        return False
    
    #Si la escrutra fue exitosa retorno correspondiente
    return True