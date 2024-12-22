import sqlite3
from conexion import conexion
def crearTabla():
    cursor = conexion()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Productos (
                ID INTEGER PRIMARY KEY,
                Nombre VARCHAR(50) NOT NULL,
                Descripcion TEXT,
                Cantidad INT NOT NULL,
                Precio REAL NOT NULL,
                Categoria TEXT)""")
    cursor.close()
