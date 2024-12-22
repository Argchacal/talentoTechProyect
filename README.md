# talentoTechProyect

Funcionalidades de la aplicación
● Registro de productos: La aplicación debe permitir al usuario
agregar nuevos productos al inventario, solicitando los
siguientes datos: nombre, descripción, cantidad, precio y
categoría.
● Visualización de productos: La aplicación debe mostrar todos
los productos registrados en el inventario, incluyendo su ID,
nombre, descripción, cantidad, precio y categoría.
● Actualización de productos: La aplicación debe permitir al
usuario actualizar la cantidad disponible de un producto
específico utilizando su ID.
● Eliminación de productos: La aplicación debe permitir al
usuario eliminar un producto del inventario utilizando su ID.
● Búsqueda de productos: La aplicación debe ofrecer una
funcionalidad para buscar productos por su ID, mostrando los
resultados que coincidan con los criterios de búsqueda. De
manera opcional, se puede implementar la búsqueda por los
campos nombre o categoría.
● Reporte de Bajo Stock: La aplicación debe generar un reporte
de productos que tengan una cantidad igual o inferior a un
límite especificado por el usuario.

Base de datos
● 'descripcion': Breve descripción del producto
(texto).'cantidad': Cantidad disponible del
producto (entero, no nulo).
● 'precio': Precio del producto (real, no nulo).
● 'categoria': Categoría a la que pertenece el
producto (texto).
● Crear una base de datos SQLite llamada
'inventario.db' para almacenar los datos de
los productos.
● La tabla 'productos' debe contener las
siguientes columnas:
● 'id': Identificador único del producto (clave
primaria, autoincremental).
● 'nombre': Nombre del producto (texto, no
nulo).
