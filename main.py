from appLvl2 import *


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

####################################  Inicio del programa ########################################
while True:
    #Genero una lista con la cantidad de opciones habilitadas 2 en este caso, pero el programa tendra 6 opciones en general
    opciones =["1","2","3","4","5","6"]
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
            agregarProducto()
        elif seleccion == "2":
            #genero una funcion y le paso la lista de producto a la cual mostrare su contenido
            mostrarInventario()
        elif seleccion == "3":
            #genero una funcion y le paso la lista de producto a la cual mostrare su contenido
            buscarProducto()