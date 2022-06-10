from re import S
import tkinter as tk

class aplicacion:
    def __init__(self):
        self.contador = 0
        self.ventana = tk.Tk()  #le da interfaz
        self.ventana.title("Contador")
        self.lblConta = tk.Label(self.ventana, text= self.contador, foreground="red") # se crea la etiqueta. text muestra un tipo de información que se ponga, en este caso el valor de self.contador. 
        self.lblConta.grid(row=0, column=1)
        self.btnIncr = tk.Button(self.ventana, text= "Incrementar", command= self.incrementar)
        self.btnIncr.grid(row=1, column=0)
        self.btnDecr = tk.Button(self.ventana, text= "Decrementar", command = self.decrementar)   #command puede llamar un metodo o función, y los botones reciben eventos que generan una acción.  en este caso command llamando el método según. 
        self.btnDecr.grid(row=1, column=2)# esta en la columna 3(2) porque el primer botón está en la columna 1(0) y en la segunda columna está 2(el contador, 1)
        
        self.ventana.mainloop() #inicia la ventana
        
        
        #ojo con la identación!!!!!
    def incrementar(self):
        self.contador += 1  # incrementa
        self.lblConta["text"] = self.contador
            
    def decrementar(self):
        self.contador -= 1  # decrementa
        self.lblConta["text"] = self.contador
            
        
        
intefaz = aplicacion()