################# Mi proyecto ###############################
# Al iniciar el programa, el usuario ve un menú con opciones claras:
# Agregar Producto al Inventario
# Mostrar el Inventario Completo
# Buscar un Producto
# Actualizar Información del Producto
# Eliminar Producto
# Salir

####################  condiciones  ###############################
# Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:
# El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
# Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados

def menu():
    
    print("*"*50) 
    print ("*  1.Agregar Producto al Inventario:             *")
    print ("*  2.Mostrar el Inventario Completo:             *")
   # print ("*  3.Buscar un Producto:                         *")
   # print ("*  4.Actualizar Información del Producto:        *")
   # print ("*  5.Eliminar Producto:                          *")
    print ("*  6.Salir                                       *")
    print("*"*50)
    

def agregarProducto(listaProducto):
    producto=[]
    
    nombre = input ("Ingrese nombre del producto: ")
    producto.append(nombre)
    cantidad = input ("Ingrese cantdidad disponible: ")
    producto.append(cantidad)
    precio = input ("Ingrese precio: ")
    producto.append(precio)
    
    listaProducto.append(producto)
    
    print ("********        Producto Agregado        *********")

def MostrarInventario(listaProducto):
    for i in listaProducto:
        print("*"*50) 
        print (f"********* Agregar Producto al Inventario *********")
        print (f"**  nombre del producto:{i[0]}                      ")
        print (f"**  cantdidad disponible:{i[1]}                     ")
        print (f"**  precio: {i[2]} pesos                            ")
        print("*"*50) 


####################################  Inicio del programa ########################################
#Lista de producto
listaProducto = []

while True:
    #Genero una lista con la cantidad de opciones habilitadas 2 en este caso, pero el programa tendra 6 opciones en general
    opciones =["1","2"]
    #genero una funcion para mostrar el menu
    menu()
    seleccion= input("Seleccione una opcion: ")
    #En base a mi lista y el input(seleccion de usuario) comparo si es una opcion valida o no y si no es 6(la opcion de salir)
    if (seleccion not in opciones) and (seleccion != "6"):
        #informo que no es una opcion valida y solicito nuevamente que elija la opcion correcta 
        print("* No es una opcion, seleccione una opcion valida *")
    elif seleccion == "6":
        #si la opcion es 6 salgo del programa y lo informo.
        print ("************** El programa finaliso **************")
        break
    else:
        # dependiendo de la opcion seleccionada realizare la accion mediante
        if seleccion == "1":
            #genero una funcion y le paso la lista de producto a la cual agregar los nuevos productos
            agregarProducto(listaProducto)
        elif seleccion == "2":
            #genero una funcion y le paso la lista de producto a la cual mostrare su contenido
            MostrarInventario(listaProducto)
