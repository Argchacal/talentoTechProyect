from appLvl2 import *



################# Mi proyecto ###############################
# Al iniciar el programa, el usuario ve un menú con opciones claras:
# 1.Registro de productos: 
# 2.Visualización de productos: 
# 3.Actualización de productos:
# 4.Eliminación de productos: 
# 5.Búsqueda de productos: 
# 6.Reporte de Bajo Stock: 
# 7.Salir

####################  condiciones  ###############################

# 1. Implementar una interfaz de usuario básica para interactuar con la base de datos a través de la línea de comandos (terminal). 
# La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente. 

####################################  Inicio del programa ########################################
while True:
    #Genero una lista con la cantidad de opciones habilitadas 2 en este caso, pero el programa tendra 6 opciones en general
    opciones =["1","2","3","4","5","6","7"]
    #genero una funcion para mostrar el menu
    menu()
    seleccion= input("Seleccione una opcion: ")
    #En base a mi lista y el input(seleccion de usuario) comparo si es una opcion valida o no y si no es 6(la opcion de salir)
    if (seleccion not in opciones) and (seleccion != "6"):
        #informo que no es una opcion valida y solicito nuevamente que elija la 1opcion correcta 
        print("* No es una opcion, seleccione una opcion valida *")
    elif seleccion == "7":
        #si la opcion es 7 salgo del programa y lo informo.
        print ("************** El programa finaliso **************")
        break
    else:
        # dependiendo de la opcion seleccionada realizare la accion mediante
        if seleccion == "1":
            registrarProducto()
        elif seleccion == "2":
            mostrarInventario()
        elif seleccion == "3":
            actualizarProductos()
        elif seleccion == "4":
            eliminarProductos()
        elif seleccion == "5":
            buscarProducto()
        elif seleccion == "6":
            reporteStockProductos()
