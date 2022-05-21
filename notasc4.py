#Conversiones.
cadena = "Casa"
lista = list(cadena)
print(lista)

lista2 = "-".join(lista)        #solo para str. También se pueden quitar espacios. 
print(lista2)

dicionario = dict(zip(range((len(cadena)), cadena)))
