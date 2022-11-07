# DjangoProyectBiblioteca

Segunda actividad evaluativa tendencias Desarrollo de software

Se quiere crear un programa que permita administrar una biblioteca. La biblioteca
maneja material académico de diferente tipo, libros, revistas, material audiovisual,
etc.

La aplicación debe permitir registrar nuevos materiales al catalogo de disponibilidad
y permitir el préstamo y devolución de estos materiales.

De cada material se conoce:

- Identificador. No pueden existir dos materiales en la biblioteca con el mismo
identificador
- Título. El nombre del libro.
- Fecha de registro.
- Cantidad registrada.
- Cantidad actual. Solo puede ser modificada mediante el préstamo, devolución y
adición de unidades registradas.

Solo las personas registradas pueden prestar y devolver materiales, de cada
persona se conoce:
-nombre.
-cedula. No puede haber dos personas con la misma cedula.
-Rol. Los estudiantes puedes prestar 5 materiales al tiempo, los profesores tres y
los administrativos uno. En caso de intentar prestar uno adicional debe mencionar
que no es posible.
Las personas solo pueden ser eliminadas del registro si no tienen materiales
prestados.
La biblioteca maneja un historial de movimientos donde se registran todos los
prestamos devoluciones, en este historial se guarda la información del material
prestado o devuelto, la información de la persona (nombre/cedula) que lo presta o
regresa y la fecha en la que se realiza el movimiento.

El programa debe permitir al usuario:

1. Registrar un material en el catálogo.
2. Registrar una persona.
3. Eliminar una persona.
4. Registrar un préstamo.
5. Registrar una devolución.
6. Incrementar cantidad registrada de un material en específico.
7. Consultar el historial de la biblioteca.
