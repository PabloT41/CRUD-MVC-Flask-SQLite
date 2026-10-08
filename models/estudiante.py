import sqlite3

DB= "estudiantes.db"

def obtener_conexion():
    conexion= sqlite3.connect(DB)
    conexion.row_factory= sqlite3.Row
    return conexion 

def crear_tabla():
    conexion = obtener_conexion()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            carrera TEXT NOT NULL
        )
    """) 

    conexion.commit()
    conexion.close()


# Obtener todos los estudiantes
def obtener_estudiantes():
    conexion = obtener_conexion()

    estudiantes = conexion.execute(
        "SELECT * FROM estudiantes ORDER BY id"
    ).fetchall()

    conexion.close()

    return estudiantes


# Crear un nuevo estudiante
def crear_estudiante(nombre, correo, carrera):
    conexion = obtener_conexion()

    conexion.execute(
        "INSERT INTO estudiantes (nombre, correo, carrera) VALUES (?, ?, ?)",
        (nombre, correo, carrera)
    )

    conexion.commit()
    conexion.close()

# Obtener un estudiante específico por su ID
def obtener_estudiante_por_id(id):
    conexion = obtener_conexion()

    estudiante = conexion.execute(
        "SELECT * FROM estudiantes WHERE id = ?",
        (id,)
    ).fetchone()

    conexion.close()

    return estudiante


# Actualizar los datos de un estudiante
def actualizar_estudiante(id, nombre, correo, carrera):
    conexion = obtener_conexion()

    conexion.execute(
        """
        UPDATE estudiantes
        SET nombre = ?, correo = ?, carrera = ?
        WHERE id = ?
        """,
        (nombre, correo, carrera, id)
    )

    conexion.commit()
    conexion.close() 

# Eliminar un estudiante por su ID
def eliminar_estudiante(id):
    conexion = obtener_conexion()

    conexion.execute(
        "DELETE FROM estudiantes WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()