from productos import Producto
from conexion import *
from creaBD_Tabla import *

from colorama import Back, Fore, init

print(Fore.GREEN + "Recursos Python")
init()#inicia colorama
def menu():
    #crea la tabla si no esta creada
    crearTabla()

    
    print (Fore.YELLOW + "*"*50) 
    print (Fore.YELLOW +"*                      MENU                      *")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 1.Registro de productos:                       "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 2.Visualización de productos:                  "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 3.Actualización de productos:                  "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 4.Eliminación de productos:                    "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 5.Búsqueda de productos:                       "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 6.Reporte de Bajo Stock:                       "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"+ Fore.GREEN + " 7.Salir                                        "+ Fore.YELLOW +  "*")
    print (Fore.YELLOW + "*"*50)

def registrarProducto():
    nombre = input ("Ingrese nombre del producto: ")
    descripcion = input ("Ingrese descripcion de producto: ")
    cantidad = input ("Ingrese cantidad de producto: ")
    precio = input ("Ingrese precio de producto: ")
    categoria = input ("Ingrese la categoria de producto ")
    cursor = conexion()
    cursor.execute('INSERT INTO Productos VALUES(null,?,?,?,?,?)',
                (nombre, descripcion,cantidad,precio,categoria))
    cursor.connection.commit()
    cursor.connection.close()
    print ("********        Producto Agregado        *********")

def mostrarInventario():
    cursor = conexion()
    cursor.execute('SELECT * FROM Productos')
    produc = cursor.fetchall()
    for i in produc:
        print(Fore.YELLOW + "*"*50)
        print (Fore.YELLOW + "*"+ Fore.GREEN + f"  ID: {i[0]}                                   ")
        print (Fore.YELLOW + "*"+ Fore.GREEN + f"  NOMBRE: {i[1]}                               ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  DESCRIPCION: {i[2]}                           ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  CANTIDAD: {i[3]}                              ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  PRECIO: {i[4]}                                ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  CATEGORIA: {i[5]}                             ")
        print(Fore.YELLOW + "*"*50)
    cursor.connection.close()


def buscarProducto():
    #El usuario puede ingrasar un id y actualizar la cantidad
    idProducto = input ("Ingrese el Id del producto a buscar: ")
    cursor = conexion()
    cursor.execute('SELECT * FROM Productos WHERE Id = ?', (idProducto,))
    produc = cursor.fetchall()
    for i in produc:
        print(Fore.YELLOW + "*"*50) 
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  ID: {i[0]}                                   ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  NOMBRE: {i[1]}                               ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  DESCRIPCION: {i[2]}                          ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  CANTIDAD: {i[3]}                             ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  PRECIO: {i[4]}                               ")
        print (Fore.YELLOW + "*"+ Fore.GREEN +f"  CATEGORIA: {i[5]}                            ")
        print(Fore.YELLOW + "*"*50)
    cursor.connection.close()

def eliminarProductos():
    #El usuario puede ingrasar un id y eliminarlo
    idProducto = input ("Ingrese nombre el id a eliminar: ")
    cursor = conexion()
    cursor.execute(f"DELETE FROM Productos WHERE Id = {idProducto}")
    cursor.connection.commit()
    cursor.connection.close()
    print (Fore.RED +f"*********  Producto con Id:{idProducto} Eliminado  **********")

def actualizarProductos():
    #El usuario puede ingrasar un id y modificarlo
    idProducto = input ("Ingrese nombre el id a modificar: ")
    cantNueva = input ("Ingrese la nueva cantidad del producto: ")
    cursor = conexion()
    cursor.execute(f"UPDATE Productos SET Cantidad = {cantNueva } WHERE Id = {idProducto}")
    cursor.connection.commit()
    cursor.connection.close()
    print (Fore.MAGENTA + f"********  Producto con Id:{idProducto} Modificado   *********")


def reporteStockProductos():
    #El usuario ingresa el limite de stock par mostrarlo en pantalla
    cursor = conexion()
    stock = input ("Ingrese la nueva cantidad límite especificado de producto: ")
    cursor.execute(f"SELECT * FROM Productos WHERE Cantidad <= ? ORDER BY Cantidad DESC", (stock,))
    resultados = cursor.fetchall() # Obtener todos los registros
    print (Fore.BLUE +f"********   Producto en orden decendente   *********")
    for i in resultados: # Mostrar los resultados
        print(Fore.YELLOW + "*"*50) 
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  ID: {i[0]}                                   ")
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  NOMBRE: {i[1]}                               ")
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  DESCRIPCION: {i[2]}                          ")
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  CANTIDAD: {i[3]}                             ")
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  PRECIO: {i[4]}                               ")
        print (Fore.YELLOW + "*"+ Fore.BLUE +f"  CATEGORIA: {i[5]}                            ")
        print(Fore.YELLOW + "*"*50)
    cursor.close()




