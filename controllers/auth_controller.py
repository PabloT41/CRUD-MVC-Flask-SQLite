from flask import Blueprint, render_template, request, redirect, url_for, session

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "admin" and password == "admin123":
            session["usuario"] = usuario
            return redirect(url_for("estudiantes.listar"))

        error = "Usuario o contraseña incorrectos"

    return render_template("login.html", error=error)


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))