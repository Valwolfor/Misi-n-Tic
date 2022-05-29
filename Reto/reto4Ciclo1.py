#Un contador necesita llevar una bitácora acerca de los registros diarios de una papelería, en consecuencia, esta información que necesita automatizar es la siguientes:
def ordenes(rutinaContable):
    from functools import reduce
    
    valor_Total_Codigo = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), rutinaContable))
    # print(valor_Total_Codigo) #Este da la cantidad * valor.
    total_orden = list(map(lambda x: [x[0]] + [reduce(lambda a, e:  a + e, x[1:])], valor_Total_Codigo))
    # print(total_orden) #
    total_orden = list(map(lambda x: x if x[1] >= 600000 else [x[0]]+[x[1] + 25000], total_orden))
    # print(total_orden)
    # {:,.2f} para sacar numero con , miles y 2 float, decimales.
    
    print('----------------- Inicio Registro diario --------------------------')
    for i in total_orden:  #Ayuda a imprimir todos los elementos
        print("La factura {0} tiene un total en pesos de {1:,.2f}".format(i[0], i[1]))
    print('----------------- Fin Registro diario -----------------------------')


rutinaContable = [  
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]  
]
#Este no sirve.
# registro = [
#     [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
#     [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
#     [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
#     [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
#     [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
#     [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
#     [6591, ("7812", 2, 11.99), ("9652",11,18.99)],
#     [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)], 
#     [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)]
# ]

ordenes(rutinaContable)

"""
#Está es la versión aceptada. 
def ordenes(rutinaContable):
    from functools import reduce
    
    valor_Total_Codigo = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), rutinaContable))
    total_orden = list(map(lambda x: [x[0]] + [reduce(lambda a, e:  a + e, x[1:])], valor_Total_Codigo))
    total_orden = list(map(lambda x: x if x[1] >= 600000 else [x[0]]+[x[1] + 25000], total_orden))
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in total_orden:  #Ayuda a imprimir todos los elementos
        print("La factura {0} tiene un total en pesos de {1:,.2f}".format(i[0], i[1]))
    print('-------------------------- Fin Registro diario ----------------------------------')
"""