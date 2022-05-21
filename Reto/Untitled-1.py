def CDT(nombre: str, capital: int, tiempo: int):
    #Función para calcular el monto total de cada cliente según su capital inicial más tasa de interés. 
    tasaDeInteres = 0.03
    tasaDePenalización = 0.02
   
    if tiempo > 2:
        interesesGanados = (capital * tasaDeInteres * tiempo)/12
        dineroTotal = interesesGanados + capital
        return f"Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {dineroTotal}"
    else: 
        penalizacion = tasaDePenalización * capital
        dineroTotal = capital - penalizacion
        return f"Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {dineroTotal}"
CDT("Dario", 100, 3)
print (CDT("Dario", 100, 3))