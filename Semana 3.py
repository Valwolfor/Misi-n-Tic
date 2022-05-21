# #Separar una oración en sus palabras.

# oracion = 'Mary entiende muy bien Python'
# frases = oracion.split() # convierte a una lista cada palabra
# print("La oración analizada es:", oracion, ".\n")

# for palabra in range(len(frases)):
#     print("Palabra: {0}, en la frase su posición es: {1}".format( frases[palabra], palabra)) #el .format le da formatos a los cochetes. 

#Dicionarios con FOR 
# datos_basicos = {
# "nombres":"Leonardo Jose",
# "apellidos":"Caballero Garcia",
# "cedula":"26938401",
# "fecha_nacimiento":"03/12/1980",
# "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
# "nacionalidad":"Venezolana",
# "estado_civil":"Soltero"
# }
# clave = datos_basicos.keys()
# valor = datos_basicos.values()
# cantidad_datos = datos_basicos.items()

# for clave, valor in cantidad_datos: print(clave + ": " + valor)

#reviselo mañana, no entiende nada.


# CRUD

frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
for nombre, color in frutas.items():
    print(nombre, "es de color", color)