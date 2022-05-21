#Función para registrar unas ventas y luego poder encontrarlas desde un producto específico. Esto

def AutoPartes(ventas:list) -> dict:
# Función de registro de ventas y conversión en dicionarion con lista de tuplas por identificación del producto (idProducto)
    partes = {}
    for i in ventas: 
        if partes.get(i[0]) == None:
            partes[i[0]] = []
        partes[i[0]].append((i[1], i[2], i[3], i[4], i[5], i[6], i[7])) #segundo parentesis indica construción tupla
    
    return partes

def consultaRegistro(ventas, idProducto) -> str:
# Permite consulta mediante la identificación del producto en la lista de entrada, buscar dentro del dicionario creado en la función AutoPartes().
    if idProducto in ventas:
        for i in ventas[idProducto]:
            print(f"Producto consultado : {idProducto}  Descripción  {i[0]}  #Parte  {i[1]}  Cantidad vendida  {i[2]}  Stock  {i[3]}  Comprador {i[4]}  Documento  {i[5]}  Fecha Venta  {i[6]}")
    else:
        print("No hay registro de venta de ese producto")


# Entrada de lista de Tuplas para convertirlas en dicionario.
# ventas = [
#     (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
#     (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
#     (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
#     (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
#     (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]

ventas = [
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]

#Llamados y salidas de la función. 
print(consultaRegistro(AutoPartes(ventas), 2001))
# print(AutoPartes(ventas))



