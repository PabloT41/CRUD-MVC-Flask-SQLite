from flask import Blueprint, render_template, request, redirect, url_for, session

from models.estudiante import (
    obtener_estudiantes,
    crear_estudiante,
    obtener_estudiante_por_id,
    actualizar_estudiante, 
    eliminar_estudiante
)


estudiantes = Blueprint("estudiantes", __name__)


# READ: mostrar todos los estudiantes
@estudiantes.route("/estudiantes")
def listar():

    # Verificar que exista una sesión iniciada
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    lista = obtener_estudiantes()

    return render_template(
        "estudiantes.html",
        estudiantes=lista
    )


# CREATE: registrar un nuevo estudiante
@estudiantes.route("/estudiantes/nuevo", methods=["GET", "POST"])
def nuevo():

    # Verificar que exista una sesión iniciada
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        carrera = request.form["carrera"]

        crear_estudiante(nombre, correo, carrera)

        return redirect(url_for("estudiantes.listar"))

    return render_template("nuevo_estudiante.html")

# UPDATE: editar un estudiante existente
@estudiantes.route("/estudiantes/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    # Verificar que exista una sesión iniciada
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    # Buscar al estudiante por su ID
    estudiante = obtener_estudiante_por_id(id)

    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        carrera = request.form["carrera"]

        # Actualizar estudiante en la base de datos
        actualizar_estudiante(id, nombre, correo, carrera)

        return redirect(url_for("estudiantes.listar"))

    return render_template(
        "editar_estudiante.html",
        estudiante=estudiante
    )

# DELETE: eliminar un estudiante
@estudiantes.route("/estudiantes/eliminar/<int:id>", methods=["POST"])
def eliminar(id):

    # Verificar que exista una sesión iniciada
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    # Eliminar estudiante de la base de datos
    eliminar_estudiante(id)

    return redirect(url_for("estudiantes.listar"))