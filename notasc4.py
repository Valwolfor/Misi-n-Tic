#Función ->map para aplicar una función sobre un objeto iterable, en cada uno de sus elementos. 
def cuadrados (elemento):
    return elemento * elemento
lista = [1, 2, 3, 4, 5, 6, 4, 6, 4, 8]

resultado = list(map(cuadrados, lista))
# print(resultado)

resultado2 = list(map(lambda elemento: elemento * elemento, lista)) # puede tener varios iterables. 
# print(resultado2)

# Función ->filter, permite filtar una función en un objeto iterable, los retornos de la función deben ser booleanos. Los True pasaran el filtro
elementos = [2, 3, 4, 5 ,6 ,7 , 1 ,45 ,7 ,8] 
resultado = list(filter(lambda elemento: elemento > 5, elementos))
# print(resultado, "\n", len(resultado))

#Función ->reduce, cuando se necesita generar un elemento de una colección. Como un acomulador. La función a aplicar debe tener mínimo 2 parametros. El primer parametro será un acomulador y el segundo el iterador. 
#reduce debe ser importado de functools. 
from functools import reduce

resultado2 = reduce(lambda acomulador, iterador: acomulador + iterador, elementos) #puede haber un tercer argumento de reduce, que es en lo que queremos que inicie o default, en lo que comience la acomulación
# print(resultado2)

#-> all, para verificar varias condiciones todas verdaderas. Vacío es True.
uids = ['B1CD102351', 'B1CDEF2354']

for iud in uids:
    #Verifica varias condiciones. 
    cond =[]
    # Mayúsculas
    cond.append(len(list(filter(lambda x: x.isupper(), list(iud)))) >=2 )
    #dígitos
    cond.append(len(list(filter(lambda x: x.isdigit(), list(iud)))) >=3 )
    #alfanumerico
    cond.append(len(list(filter(lambda x: not(x.isalnum()), list(iud)))) == 0)
    #No repeticiones
    cond.append(len(iud) == len(set(iud))) #compara los dos contenedores, pero uno es conjunto y esto no repite valores.
    #10 de longitud
    cond.append(len(iud) == 10)
    print('Valido') if all(cond) else print('Invalido')

