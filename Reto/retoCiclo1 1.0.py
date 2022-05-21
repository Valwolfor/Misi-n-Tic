#Dinero que deben recibir los clientes de un CDT bancario según su cápital de inversión, tiempo e intereses.
def CDT(nombre: str, capital: int, tiempo: int):
    #Función para calcular el monto total a cada cliente según su capital inicial más tasa de interés. 
    tasaDeInteres = 0.03
    tasaDePenalización = 0.02

    if tiempo > 2:
        interesesGanados = (capital * tasaDeInteres * tiempo)/12
        dineroTotal = interesesGanados + capital
    else: 
        penalizacion = tasaDePenalización * capital
        dineroTotal = capital - penalizacion
    return f"Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {dineroTotal}"
#Entrega de resultados.

print (CDT("DIE23CDT", 1000000, 3))

