from productos import Producto
from conexion import *
def menu():
    print("*"*50) 
    print ("*  1.Agregar Producto al Inventario:             *")
    print ("*  2.Mostrar el Inventario Completo:             *")
    print ("*  3.Buscar un Producto:                         *")
   # print ("*  4.Actualizar Información del Producto:        *")
   # print ("*  5.Eliminar Producto:                          *")
    print ("*  6.Salir                                       *")
    print("*"*50)
    

def agregarProducto():
    nombre = input ("Ingrese nombre del producto: ")
    descripcion = input ("Ingrese descripcion de producto: ")
    precio = input ("Ingrese precio: ")
    categoria = input ("Ingrese la categoria: ")
    cursor = conexion()
    cursor.execute('INSERT INTO Productos VALUES(null,?,?,?,?)',
                (nombre, descripcion,precio,categoria))
    cursor.connection.commit()
    cursor.close()
    print ("********        Producto Agregado        *********")

def mostrarInventario():
    cursor = conexion()
    cursor.execute('SELECT * FROM Productos')
    produc = cursor.fetchall()
    for i in produc:
        
        print("Id:", i[0],"Nombre:",i[1],"Descripcion:", i[2],"Precio:", i[3],"Categoria:", i[4])

def buscarProducto():
    nombre = input ("Ingrese nombre del producto a buscar: ")
    cursor = conexion()
    cursor.execute('SELECT * FROM Productos WHERE nombre = ?', (nombre,))
    produc = cursor.fetchall()
    print(produc)



