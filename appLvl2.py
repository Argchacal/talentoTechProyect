from productos import Producto
from conexion import *
from creaBD_Tabla import *
def menu():
    #crea la tabla si no esta creada
    crearTabla()
    print("*"*50) 
    print ("*                      MENU                      *")
    print ("*  1.Registro de productos:                      *")
    print ("*  2.Visualización de productos:                 *")
    print ("*  3.Actualización de productos:                 *")
    print ("*  4.Eliminación de productos:                   *")
    print ("*  5.Búsqueda de productos:                      *")
    print ("*  6.Reporte de Bajo Stock:                      *")
    print ("*  7.Salir                                       *")
    print("*"*50)

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
        print("*"*50) 
        print (f"*  ID: {i[0]}                                   ")
        print (f"*  NOMBRE: {i[1]}                               ")
        print (f"*  DESCRIPCION: {i[2]}                          ")
        print (f"*  CANTIDAD: {i[3]}                             ")
        print (f"*  PRECIO: {i[4]}                               ")
        print (f"*  CATEGORIA: {i[5]}                            ")
        print("*"*50)
    cursor.connection.close()


def buscarProducto():
    #El usuario puede ingrasar un id y actualizar la cantidad
    idProducto = input ("Ingrese el Id del producto a buscar: ")
    cursor = conexion()
    cursor.execute('SELECT * FROM Productos WHERE Id = ?', (idProducto,))
    produc = cursor.fetchall()
    for i in produc:
        print("*"*50) 
        print (f"*  ID: {i[0]}                                   ")
        print (f"*  NOMBRE: {i[1]}                               ")
        print (f"*  DESCRIPCION: {i[2]}                          ")
        print (f"*  CANTIDAD: {i[3]}                             ")
        print (f"*  PRECIO: {i[4]}                               ")
        print (f"*  CATEGORIA: {i[5]}                            ")
        print("*"*50)
    cursor.connection.close()

def actualizarProductos():
    #El usuario puede ingrasar un id y actualizar la cantidad
    idProducto = input ("Ingrese nombre el id a modificar: ")
    cantNueva = input ("Ingrese la nueva cantidad del producto: ")
    cursor = conexion()
    cursor.execute(f"UPDATE Productos SET Cantidad = {cantNueva } WHERE Id = {idProducto}")
    cursor.connection.commit()
    cursor.connection.close()
    print (f"********        Producto con Id:{idProducto} Modificado        *********")

def eliminarProductos():
    #El usuario puede ingrasar un id y eliminarlo
    idProducto = input ("Ingrese nombre el id a eliminar: ")
    cursor = conexion()
    cursor.execute(f"DELETE FROM Productos WHERE Id = {idProducto}")
    cursor.connection.commit()
    cursor.connection.close()
    print (f"********        Producto con Id:{idProducto} Eliminado        *********")

def actualizarProductos():
    #El usuario puede ingrasar un id y modificarlo
    idProducto = input ("Ingrese nombre el id a modificar: ")
    cantNueva = input ("Ingrese la nueva cantidad del producto: ")
    cursor = conexion()
    cursor.execute(f"UPDATE Productos SET Cantidad = {cantNueva } WHERE Id = {idProducto}")
    cursor.connection.commit()
    cursor.connection.close()
    print (f"********        Producto con Id:{idProducto} Modificado        *********")


def reporteStockProductos():
    #El usuario ingresa el limite de stock par mostrarlo en pantalla
    cursor = conexion()
    stock = input ("Ingrese la nueva cantidad límite especificado de producto: ")
    
    cursor.execute(f"SELECT * FROM Productos WHERE Cantidad <= {stock} ORDER BY Cantidad DESC")
    resultados = cursor.fetchall() # Obtener todos los registros
    for i in resultados: # Mostrar los resultados
        print("*"*50) 
        print (f"*  ID: {i[0]}                                   ")
        print (f"*  NOMBRE: {i[1]}                               ")
        print (f"*  DESCRIPCION: {i[2]}                          ")
        print (f"*  CANTIDAD: {i[3]}                             ")
        print (f"*  PRECIO: {i[4]}                               ")
        print (f"*  CATEGORIA: {i[5]}                            ")
        print("*"*50)
    cursor.close()




