#Entradas al parqué AVENTURAS EXTREMAS, una función que recibe dicionario para verificar :
#Edad, primer_ingreso. 
#El valor se puede ver variado según descuento 5% : X-Treme, 7% : carros chocones, 5% : sillas voladoras.  
#Diccionario para datos del cliente.

def cliente(informacion:dict)->dict:
    #Func para verificar costo e ingreso a las atracciones.
    #Verificación de apto según edad. 
    if informacion["edad"] > 18:
        apto = True
        atraccion = "X-Treme"
        if informacion["primer_ingreso"] == True:
            total_boleta = 20000 - (20000 * 0.05)
        else:
            total_boleta = 20000
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
        apto = True
        atraccion = "Carros chocones"
        if informacion["primer_ingreso"] == True:
            total_boleta = 5000 - (5000 * 0.07)
        else:
            total_boleta = 5000
    elif informacion["edad"] >= 7 and informacion["edad"] < 15:
        apto = True
        atraccion = "Sillas voladoras"
        if informacion["primer_ingreso"] == True:
            total_boleta = 10000 - (10000 * 0.05)
        else:
            total_boleta = 10000
    else:
        apto = False
        primer_ingreso = False
        atraccion = "N/A"
        total_boleta ="N/A"
    #Nuevo diccionario de salida.
    salida = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        "atraccion": atraccion,
        "apto": apto,
        "primer_ingreso": informacion["primer_ingreso"],
        "total_boleta": total_boleta
    }
    return  salida

cliente(informacion)
print(cliente(informacion))
