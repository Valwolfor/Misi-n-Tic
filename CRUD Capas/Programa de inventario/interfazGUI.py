#Librería para interacción por consola (interfaz no ejecutable)
#################################################

#Librerías con las clases para construir los widgets (ventanas, botones, cambos, labels, etc)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Librería para interactuar con el backend
import CRUD_inventario as CRUD

#Función para crear la tabla de tareas en la estructura tipo treeview
def generarTablaListadoProductos(marcoInteraccion,producto):

    #Instanciado del treeview, permite jerarquía pero se utilizará como una tabla para las tareas
    TablaProductos = ttk.Treeview(marcoInteraccion)

    #Especificación de las columnas
    TablaProductos['columns'] = ('Nombre', 'Cantidad', 'Costo', 'En nevera', 'En almancen')
    TablaProductos.column('Nombre', width=0, stretch=tk.NO)
    TablaProductos.column('Cantidad', anchor=tk.CENTER, width=100)
    TablaProductos.column('Costo', anchor=tk.W, width=300)
    TablaProductos.column('En nevera', anchor=tk.W, width=100)
    TablaProductos.column('En almacen', anchor=tk.CENTER, width=100)

    #Especificación del encabezado
    TablaProductos.heading('Nombre', text='Nombre del producto', anchor=tk.CENTER)
    TablaProductos.heading('Cantidad', text='Cantidad total', anchor=tk.CENTER)
    TablaProductos.heading('Costo', text='Costo del producto ', anchor=tk.W)
    TablaProductos.heading('En nevera', text='Cantidad en la nevera actualmente:', anchor=tk.CENTER)
    TablaProductos.heading('En almacen', text='Cantidad en almacen actualmente:', anchor=tk.CENTER)    

    #Insertar el listado de productos cargado en memoria proveniente de la capa de datos en la tabla
    indiceNumerico = 0
    for identificador, producto in producto.items():
        TablaProductos.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, producto['Nombre'], producto['Cantidad'], producto['Costo'], producto['En nevera'], producto['En almacen']) )
        indiceNumerico += 1       

    #Retornar el objeto para las actualizaciones que se generen por los eventos
    return TablaProductos

#Función para creación de la ventana o menú principal
def ventanaMenuPrincipal(producto):

    #Crear el objeto de la ventana principal
    m = tk.Tk()
    m.title('Registro de bebidas Tonika')#Especificar el título de la ventana       

    ######## Composición de widgets y procedimientos para el funcionamiento de la interfaz ########

    #Crear los marcos para agrupar visualmente los widgets
    marcoInteraccion = ttk.Frame(m, borderwidth=2, relief="raised", padding=(10,10))#Formulario    
    marcoCRUD = ttk.Frame(m, borderwidth=2, relief="raised", padding=(10,10))#Acciones   

    #Crear tabla de produdtos
    TablaProductos = generarTablaListadoProductos(marcoInteraccion,producto)

    #Agregar entradas para los atributos de los productos

    #Id Producto   
    etiquetaId = tk.Label(marcoInteraccion, text = 'Nombre')    
    entradaId = tk.Entry(marcoInteraccion)   

    #Cantidad del producto
    etiquetaCantidad = tk.Label(marcoInteraccion, text = 'Cantidad:')    
    entradaCantidad = tk.Entry(marcoInteraccion)    
    
    #Costo
    etiquetaCosto = tk.Label(marcoInteraccion, text = 'Costo:')    
    entradaCosto = tk.Entry(marcoInteraccion)    

    #En nevera
    etiquetaNevera = tk.Label(marcoInteraccion, text = 'Hay en nevera:')    
    entradaNevera = tk.Entry(marcoInteraccion)
    
    #En almacen
    etiquetaAlmacen = tk.Label(marcoInteraccion, text = 'Hay en almancen')    
    entradaAlmacen = tk.Entry(marcoInteraccion)   

    #Función que limpia los campos del formulario (marcoInteraccion)
    def limpiarCampos():        
        entradaId.delete(0,tk.END)
        entradaCantidad.delete(0,tk.END)
        entradaCosto.delete(0,tk.END)
        entradaNevera.delete(0,tk.END)
        entradaAlmacen.delete(0,tk.END)    

    #Botón para limpiar los campos
    btnLimpiarCampos = tk.Button(marcoInteraccion, text='Limpiar Campos', command = limpiarCampos )

    #Cargar información de la tarea seleccionada
    def cargarTareaSeleccionada():        
        
        #Extraer información de la interfaz
        seleccionada = TablaProductos.focus()
        infoSeleccionada = TablaProductos.item(seleccionada, 'values')

        #Limpiar los campos
        limpiarCampos()

        #Cargar la información extraída
        entradaId.insert(0,infoSeleccionada[0])        
        entradaCantidad.insert(0,infoSeleccionada[1])        
        entradaCosto.insert(0,infoSeleccionada[2])
        entradaNevera.insert(0,infoSeleccionada[3])
        entradaAlmacen.insert(0,infoSeleccionada[4])
    
    #Botón para cargar la tarea seleccionada
    btnCargarProductosSeleccionados = tk.Button(marcoInteraccion, text='Cargar Info Tarea Seleccionada', command = cargarTareaSeleccionada)

    #Ubicación de los elementos (frame para el formulario) de interacción en la ventana principal 
    marcoInteraccion.grid(column=0, row=0)    
    TablaProductos.grid(column=0,row=0,columnspan=3)    
    etiquetaId.grid(column=0,row=1,sticky=tk.W)
    entradaId.grid(column=1,row=1)
    etiquetaCantidad.grid(column=0,row=2,sticky=tk.W)
    entradaCantidad.grid(column=1,row=2)
    etiquetaCosto.grid(column=0,row=3,sticky=tk.W)
    entradaCosto.grid(column=1,row=3)
    etiquetaNevera.grid(column=0,row=4,sticky=tk.W)
    entradaNevera.grid(column=1,row=4)
    etiquetaAlmacen.grid(column=0,row=5,sticky=tk.W)
    entradaAlmacen.grid(column=1,row=5)
    btnCargarProductosSeleccionados.grid(column=2,row=2)
    btnLimpiarCampos.grid(column=2,row=3)    

    ######## Composición de widgets y procedimientos para las operaciones CRUD en la Interfaz ########  

    #Función intermediaria para preparar información recogida de los campos como la espera el CRUD
    #Redirige la información encapsulada a los eventos especificados en los botones
    #Será utilizada por todas las operaciones Create, Update y Delete
    def encapsularInfoFormulario(accion):

        #Obtener el identificador de las entradas
        identificador = entradaId.get()
                
        #Encapsular información
        infoCampos = {            
            'Cantidad' : entradaCantidad.get(),
            'Costo' : entradaCosto.get(),
            'En nevera' : entradaNevera.get(),
            'En almacen' : entradaAlmacen.get()
        }

        #Revisar evento del botón para iniciar las acciones correspondientes en las otras capas
        if accion == "Create":

            #Llamar la función que realiza la actualización de la vista y el backend
            adicionarProducto(TablaProductos, producto, identificador, infoCampos)
        
        elif accion == "Update":
            
            #Llamar la función que realiza la actualización de la vista y el backend
            actualizarProducto(TablaProductos, producto, identificador, infoCampos)
        
        elif accion == "Delete":
            
            #Llamar la función que realiza la actualización de la vista y el backend
            eliminarProducto(TablaProductos, producto, identificador, infoCampos)
    
    #Función que realiza la adición de la tarea en la vista y el backend
    def adicionarProducto(TablaProductos, producto, identificador, productoNuevo): 

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos() 

        #Actualizar el widget correspondiente en la interfaz
        indiceNumerico = len(TablaProductos.get_children())   
        TablaProductos.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, productoNuevo['Cantidad'], productoNuevo['Costo'],productoNuevo['En nevera'], productoNuevo['En almacen']) )

        #Llamar el backend para actualizar el contenedor de las tareas
        CRUD.Create(producto, identificador, productoNuevo) 

    #Botón para adición de producto, desencadenando los eventos en las demás capas    
    btnAdicionarProducto = tk.Button(marcoCRUD, text='Adicionar Producto', command = lambda : encapsularInfoFormulario("Create")  )

    #Función que realiza la actualización de la tarea cargada en la vista y el backend
    def actualizarProducto(TablaProductos, producto, identificador, productoNuevo):

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos()        

        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaProductos.get_children():
            TablaProductos.delete(i)
        
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Update(producto, identificador, productoNuevo)

        #Insertar en la vista todas las tareas que están cargadas en memoria
        indiceNumerico = 0
        for identificador, producto in producto.items():
            TablaProductos.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, productoNuevo['Cantidad'], productoNuevo['Costo'],productoNuevo['En nevera'], productoNuevo['En almacen']) )
            indiceNumerico += 1   
    
    #Botón para actualización de tarea, desencadenando los eventos en las demás capas    
    btnActualizarProducto = tk.Button(marcoCRUD, text='Actualizar Producto', command = lambda : encapsularInfoFormulario("Update")  )

    #Función que realiza la eliminación de la tarea cargada en la vista y el backend
    def eliminarProducto(TablaProductos, producto, identificador, productoNuevo):    

        #Actualizar la interfaz acorde a la operación solicitada

        #Limpiar los campos de la interfaz
        limpiarCampos() 

        #Eliminar todos los elementos (filas o hijos) de la tabla de la interfaz
        for i in TablaProductos.get_children():
            TablaProductos.delete(i)
        
        #Actualizar el contenedor cargado en memoria (llamado a backend)
        CRUD.Delete(producto, identificador)        

        #Insertar en la vista todas las tareas que están cargadas en memoria posterior a la eliminación
        indiceNumerico = 0
        for identificador, producto in producto.items():
            TablaProductos.insert(parent='', index=indiceNumerico, iid=indiceNumerico, text='', values=(identificador, productoNuevo['Cantidad'], productoNuevo['Costo'], productoNuevo['En nevera'], productoNuevo['En almacen']) )
            indiceNumerico += 1
    
    #Botón para eliminación de tarea, desencadenando los eventos en las demás capas    
    btnEliminarProducto = tk.Button(marcoCRUD, text='Eliminar Producto', command = lambda : encapsularInfoFormulario("Delete")  )
    
    #Función que guarda los cambios y cierra la aplicación
    def salirGuardar():

        #Solicitar al backend que actualice la base de datos
        CRUD.Write(producto)

        #Informar a través de la interfaz gráfica
        messagebox.showinfo(message="Información guardada en capa de datos", title="Cierre Sesión")       

        #Cerrar la ventana
        m.destroy()

    #Botón para salir y guardar cambios
    btnSalirGuardar = tk.Button(marcoCRUD, text='Salir y Guardar', command = salirGuardar  )

    #Carga de imagen para asociar a widget tipo etiqueta    
    from PIL import ImageTk,Image #Librería para procesar formato png y redimensionar
    #Proporciones de la imagen
    w = 140 
    h = 140   
    imagenCargada = Image.open("logoTonika.jpg")#Carga de la imagen
    imagenCargada.thumbnail((w,h))#Redimensionado de la imagen a las proporciones establecidas
    imagenDiscoBar = ImageTk.PhotoImage(imagenCargada)#Encapsular para tkinter
    #Creación de la etiqueta 
    etiquetaDiscoBar = tk.Label(marcoCRUD) #ensayar nombre
    #Asociación de la imagen a la etiqueta    
    etiquetaDiscoBar.config(image=imagenDiscoBar, width=w, height=h)    
    etiquetaDiscoBar.image = imagenDiscoBar

    #Etiqueta informativa funcionamiento App
    mensajeFuncionamiento = "-> Cargar Info antes de CRUD"
    etiquetaFuncionamiento = tk.Label(marcoCRUD,text=mensajeFuncionamiento)
    
    #Ubicación de los botones del CRUD    
    marcoCRUD.grid(column=1, row=0, rowspan=5, sticky=tk.N+tk.S)
    etiquetaDiscoBar.grid(column=1,row=0,sticky=tk.W+tk.E)    
    btnAdicionarProducto.grid(column=1,row=1, sticky=tk.W+tk.E)
    btnActualizarProducto.grid(column=1,row=2, sticky=tk.W+tk.E)
    btnEliminarProducto.grid(column=1,row=3, sticky=tk.W+tk.E)
    btnSalirGuardar.grid(column=1,row=4, sticky=tk.W+tk.E)
    etiquetaFuncionamiento.grid(column=1,row=5)    
    
    #Retornar la ventana de la App construída con todos los elementos y funcionalidades al controlador, para que inicie el mainloop
    return m
