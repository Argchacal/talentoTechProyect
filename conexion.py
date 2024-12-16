import sqlite3

def conexion():
    try:
        conexion = sqlite3.connect("DataBase/inventario.DB")
        cursor = conexion.cursor()
        
        

    except Exception as ex:
        #imprime la exepcion 
        print(ex)
    
    return cursor
