import tkinter as tk
from tkinter import ttk
from tkinter import *
import json

"""
Aplicación con OOP para inventario.
"""

#Objeto de la ventana de visualización. 
class Producto:
    
    def __init__(self, ventana):
        self.ven = ventana
        self.ven.title('Registro de Productos')
        
        #Un Frame para los primeros elementos. 
        seccion = LabelFrame(self.ven, text='Ingresar nuevo producto')
        seccion.grid(row=0, column=0, columnspan=4, pady=20, padx=15) #Parrilla que se ubica en lo señalado con 3 espacios de la columna y un rellendo de 20. 
        
        #dentro del Frame
        #se crea un input del nombre. 
        Label(seccion, text='Nombre: ', ).grid(row=1, column=0)
        self.nombre = Entry(seccion)
        self.nombre.focus()# hace que el cursor se poca titilante cuando se coloca en encima. Desde la ejecución
        self.nombre.grid(row=1, column=1)
        
        #input de precio
        Label(seccion, text='Precio neto: ', ).grid(row=2, column=0)
        self.precio = Entry(seccion)
        self.precio.grid(row=2, column=1)
        
        #input cantidad
        Label(seccion, text='Cantidad: ', ).grid(row=3, column=0)
        self.cantidad = Entry(seccion)
        self.cantidad.grid(row=3, column=1)
        
        #botón para ejecutar datos. 
        ttk.Button(ventana, text="Guardar nuevo producto", command= self.agregar_producto).grid(row=4, columnspan=4, sticky= W + E) #ta pendiente command, La w y e simbolizan el este y oeste para el ancho del botón.
        
        #Tabla
        self.arbol = ttk.Treeview(height=10, columns= (0, 1)) #aquí mete una columna de más.
        self.arbol.grid(row=5, column= 0, columnspan=4)
        self.arbol.heading('#0', text="Nombre", anchor=CENTER)
        self.arbol.heading('#1', text="Precio neto", anchor=CENTER)
        self.arbol.heading('#2', text="Cantidad", anchor=CENTER)
        
    
    #Validación 
    def validacion(self):
        return len(self.nombre.get()) != 0 and len(self.precio.get()) != 0 and len(self.cantidad.get()) != 0
    
    #Agregar datos
    def agregar_producto(self):
        if self.validacion():
            print(self.nombre.get())
            print(self.precio.get())
            print(self.cantidad.get())
        else:
            print("Todos los datos son requeridos.")
    
    #Creación de archivo csv. 
    def almacenamiento(self):
        datos = {}
        try:
            with open('Registros', 'w') as archivo_json:
                json.dump(datos, archivo_json)
        except:
            print("Error: No se pudo guardar la información en la capa de datos.")
        return datos
        
        
if __name__ == '__main__':
        ventana = Tk() #Se vuelve un tk la ventana. Tk es con la t en mayúscula. 
        aplicacion = Producto(ventana) #se instancia aplicacion.  
        ventana.mainloop()
    
    
    #Tengo que aprende de tkinter antes :D
    