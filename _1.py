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



##Sensores alarma
    # sensor --> puerta abierta = True 
    # sensor --> ventana abierta = fal
# puerta = True
# ventana = True

# if puerta or not(ventana):          #negación 
#     print("Alarma encendida")
# else:
#     print("Alarma apagada")




#Solución simple, con función, con llamada de función externa, recursividad, modulos
#PESO de libra a kilos.
# libra = 2
# libraEnKilos = 0.453592
# libraAKilos = libra * libraEnKilos
# print(libraAKilos)
# #raiz
# a = int(input("Numero 1"))
# b = int(input("Numero 2"))
# c = (a**2 + b**2)**0.5  
# print (c)       
# #millas kilometros
# 1 milla son 1.60934 kilómetros 
# 1 kilómetro es 0.621371 milla


#NUMERO MAYOR Y MENOR

# canNumero = int(input("ingrese el primer numero :\n"))
# for i in range(1, canNumero+1):
#     numero = int(input(f"ingrese el numero {i} \n"))
#     if i == 1:
#         menor = numero
#     else: 
#         if numero < menor:
#             menor = numero
# print(f"El menor de los {canNumero} es {menor}")

#Convertir notas de 1 a 5 con decimal a letras. 1-2.9=D; 3-3.5=R, 3.6-4=B; 4.1-5=E
# notaObtenida = float(input("Ingrese la nota a convertir."))

#EJERCICIO
#Encontrar la énesima potencia a que se debe elevar x para que sea igual a y
# def matematicoPereirano(x,y)->bool:
#     n = 1
    
#     if y <= 1:
#         return f"ingresó el valor {y}, el número debe ser superior a 1 y mayor a {x}."
        
#     for i in range(y):
        
#         if n < y:
#             n*= x
#         elif n == y:
#             return True
#         else:
#             return False

# x = int(input("Ingrese el número que elevado a la énesima potencia puede ser igual a 'y'.\n"))
# y = int(input("Ingrese el número que debe ser igual a 'x' elevado a la énesima potencia.\n"))
# matematicoPereirano(x,y)
# print(matematicoPereirano(x, y))


# EJERCICIO 2
# Clasificar chocolates
# def palidromo(numero:int)->bool:        #El simbolo -> cambia el retorno de la función.
#     centena=numero//100
#     decena=(numero-centena*100)//10
#     unidad=numero-centena*100-decena*10

#     if centena == unidad:
#         resultado = True
#     else:
#         resultado = False
#     return resultado

# def espar(numero:int)->bool:
#     if numero % 2 == 0:
#         resultado = True
#     else:
#         resultado = False
#     return resultado

# def clasificar_chocolate(codigo:int)->str:
#     if palidromo(codigo):
#         if espar(codigo):
#             resultado = "SWEET"
#         else:
#             resultado = "BITTER"
#     else:
#         if espar(codigo):
#             resultado = "CINNAMON"
#         else:
#             resultado = "LIGHT"
#     return resultado            

# print(clasificar_chocolate(123))
# print(clasificar_chocolate(222))   
# print(clasificar_chocolate(111))
# print(clasificar_chocolate(505)) 
# print(clasificar_chocolate(576)) 