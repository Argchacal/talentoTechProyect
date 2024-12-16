import sqlite3
from conexion import conexion

cursor = conexion()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS Productos (
            ID INTEGER PRIMARY KEY,
            Nombre VARCHAR(50) NOT NULL,
            Descripcion TEXT,
            Precio REAL,
            Categoria VARCHAR(20))""")

cursor.close()



# ejemplo1 = Producto("Leche", "Leche entera de 1 litro", 99, "Lácteo")
# ejemplo2 =    Producto("Pan", "Pan blanco en rebanadas", 50, "Panadería")
# ejemplo3 =    Producto("Manzana", "Manzana roja fresca", 30, "Fruta")
# ejemplo4 =    Producto("Arroz", "Arroz largo fino de 1kg", 120, "Grano")
# ejemplo5 =    Producto("Queso", "Queso mozzarella", 200, "Lácteo"),
# ejemplo6 =    Producto("Aceite", "Aceite de girasol 1L", 250, "Aceites")