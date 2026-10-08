from flask import Flask, redirect, url_for, session
from models.estudiante import crear_tabla
from controllers.auth_controller import auth
from controllers.estudiante_controller import estudiantes

app = Flask(__name__)

# Clave utilizada por Flask para manejar las sesiones
app.secret_key = "clave_secreta_deber_mvc"

# Registrar el controlador de autenticación
app.register_blueprint(auth)
app.register_blueprint(estudiantes)
# Crear la tabla de estudiantes
crear_tabla()


@app.route("/")
def inicio():

    # Si el usuario no ha iniciado sesión, enviarlo al login
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    return f"""
        <h1>Sistema de Gestión de Estudiantes</h1>
        <p>Bienvenido, {session['usuario']}</p>
        <a href="/logout">Cerrar sesión</a>
    """


if __name__ == "__main__":
    app.run(debug=True)