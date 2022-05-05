#Dinero que deben recibir los clientes de un CDT bancario según su cápital de inversión, tiempo e intereses. 
def CDT(nombre: str, capital: int, tiempo: int):
    #Función para calcular el monto total a cada cliente según su capital inicial más tasa de interés. 
    tasaDeInteres = 0.03
    tasaDePenalización = 0.02
   
    if tiempo > 2:
        interesesGanados = (capital * tasaDeInteres * tiempo)/12
        dineroTotal = interesesGanados + capital
        print("Para el usuario", nombre, ", la cantidad de dinero a recibir, según el monto inicial de ", capital, " para un tiempo de ", tiempo, " meses es: ", dineroTotal)
    else: 
        penalizacion = tasaDePenalización * capital
        dineroTotal = capital - penalizacion
        print("Para el usuario", nombre, ", la cantidad de dinero a recibir, según el monto inicial", capital, "para un tiempo de ", tiempo, " meses es: ", dineroTotal)

#Entrega de resultados.
CDT("DIE23CDT", 1000000, 2)