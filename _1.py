#Programa para identificar si un número es mayor o igual a 100.
# from re import I


# numero = int(input("Por favor ingrese un número"))
# if numero >= 100:
#     print ("El número ingrsado es mayor o igual que 100")
# else:
#     print ("El número ingrsado es menor a 100")
#Casting, es un término usado para identificar que se le modifica el tipo a una variable. 

#Ciclo While
# i = 1

# while i >= 10:
#     print (i)
#     i += 1

#Ciclo For
# for i in range(1, 10, 3): #si se coloca un tercer argumento se indica el salto
#     print(i)


#PROGRAMA DE DECLARACIÓN DE RENTA:
# edad = int(input("Ingrese la edad del usuario: "))
# ingresos   = int(input("Digite sus ingresos mensuales sin puntos"))
# ingresoAnual = ingresos * 12

# if edad > 17 and ingresoAnual >= 50831000:
#     print("Debe declarar renta. ;)")
# else:
#     print ("No debe presentar declaración de renta.")

#FUNCIONES
# def suma(x, y):
#     return x + y            #para manterner los datos guardados en la Func llamada
    
# suma(12, 35)                #así se mantiene
# print(suma(23, 77))



# def raizCuadrada():
#     valor = float(input("Por favor, ingrese un número para calcular su raiz cuadrada: "))
#     raiz = valor ** 0.5
#     return print("La raiz cuadrada de : ", valor, " es ", raiz) #¿?
# raizCuadrada()

# def otra_suma(numero1, numero2):
#     print(numero1 + numero2)
#     print("\n")
#     resultado = otra_suma(5,6)
#     print(resultado)
# def otra_suma(numero1,numero2):
#     print(numero1 + numero2)
#     print("\n")
#     return numero1 + numero2
# otra_suma(5, 6)

# def primeraFuncion():               #Función anidada con cambio de función externa en la interna.
#     x = 2
#     def segundaFuncion(a):
#         x = 6
#         print(a + x)
#     print(x)
#     segundaFuncion(3)
# primeraFuncion()

# def primerNumero(x):
#     def segundoNumero(y):
#         return x * y
#     return segundoNumero
# resultado = primerNumero(2)

# print(resultado(5))                 #necesita explicación!!!  


#MóDULOS: Dividir un código, se llaman con "import" más el nombre de modulo, importante tenerlo documentado. 
    #namespace, preguntar!!
#Los modulos puede importar solo una función o elemento. 
#2 from nombreModulo import elementoEspecificoAImportar
#3 from nombreModulo import *           #El * asterisco indica importar todas las entidades del modulo
    #aliasing(renombrar), para cambiar el nombre del módulo}
    #4 import nombreModulo as alias
        #si se desea cambiar la entidá del modulo
        #4.1.1 from module import nombre as alias
        #4.1.2 from module import n as a, m as b, o as c
        #4.1.3 from math import pi as PI, sin as sine

#Ejecutar para entender. Se colocan al final del último argumento de la func. 
# print("Mi nombre es", "Python.", end=" ")
# print("Mi nombre es", "Python.", end="\n")
# print("Mi nombre es ", end="")
# print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
# print("Mi", "nombre", "es", "Monty", "Python.", sep="*")
# print("Mi", "nombre", "es", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")
# print("Fundamentos","Programación","en", sep="_", end="_")
# print("Me gusta \"Monty Python\"")
# print('Me gusta "Monty Python')
# print(True > False)
# print(True < False)
# print('\"Estoy\" \n\"\"aprendiendo\"\" \n\"\"\"Python\"\"\'')

# from random import *
# print(randrange(1), end = ' ')
# print(randrange(0, 20), end=' ')
# print(randrange(0, 5, 1), end=' ')
# print(randint(0, 2))

