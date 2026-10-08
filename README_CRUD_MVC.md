# Sistema de Gestión de Estudiantes — CRUD MVC

Aplicación web desarrollada con **Python, Flask y SQLite** para administrar registros de estudiantes mediante las operaciones **crear, consultar, actualizar y eliminar (CRUD)**. El proyecto organiza sus responsabilidades con el patrón **Modelo–Vista–Controlador (MVC)** e incluye una pantalla de inicio de sesión.

> **Alcance:** proyecto académico y demostrativo. La autenticación actual usa credenciales definidas en el código; no está preparada para producción.

## Funcionalidades

- **Inicio de sesión:** valida las credenciales antes de permitir el acceso al módulo de estudiantes y muestra un aviso cuando son incorrectas.
- **Listado:** consulta y muestra los estudiantes registrados.
- **Registro:** permite añadir un estudiante con nombre, correo y carrera.
- **Edición:** permite modificar la información de un estudiante existente.
- **Eliminación:** borra el registro seleccionado mediante una solicitud POST.
- **Cierre de sesión:** elimina la sesión activa y regresa al formulario de acceso.
- **Interfaz:** plantillas HTML con estilos CSS. La versión visual actual utiliza una paleta morada y botones diferenciados por acción.

## Tecnologías

| Tecnología | Uso |
| --- | --- |
| Python | Lógica de la aplicación |
| Flask | Servidor web, rutas, sesiones y controladores |
| SQLite | Base de datos relacional local |
| HTML y Jinja2 | Vistas y renderizado de información |
| CSS | Presentación y diseño visual |

## Arquitectura MVC

**Modelo (`models/estudiante.py`)**: abre conexiones con SQLite, crea la tabla si no existe y ejecuta las consultas `SELECT`, `INSERT`, `UPDATE` y `DELETE`.

**Vista (`templates/`)**: contiene el formulario de acceso, el listado y los formularios para crear y editar estudiantes. Las plantillas usan Jinja2 para presentar los datos enviados por Flask.

**Controlador (`controllers/`)**: `auth_controller.py` gestiona el acceso y la salida; `estudiante_controller.py` implementa las rutas del CRUD, verifica la sesión y llama a las funciones del modelo.

**Aplicación (`app.py`)**: inicializa Flask, registra los *Blueprints* y prepara la tabla de estudiantes.

### Estructura de carpetas

```text
CRUD_MVC/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── controllers/
│   ├── auth_controller.py
│   └── estudiante_controller.py
├── models/
│   └── estudiante.py
├── templates/
│   ├── login.html
│   ├── estudiantes.html
│   ├── nuevo_estudiante.html
│   └── editar_estudiante.html
└── static/
    └── style.css
```

El archivo `estudiantes.db` se genera localmente al ejecutar la aplicación y **no debe subirse** al repositorio.

## Base de datos

La aplicación crea una tabla `estudiantes` con los siguientes campos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | INTEGER | Clave primaria autoincremental |
| `nombre` | TEXT | Nombre del estudiante; obligatorio |
| `correo` | TEXT | Correo electrónico; obligatorio |
| `carrera` | TEXT | Carrera; obligatoria |

> El ID interno no se reutiliza automáticamente al borrar registros. Si la interfaz muestra números consecutivos mediante `loop.index`, esa numeración es visual y no modifica la clave primaria.

## Instalación y ejecución local

### Requisitos

- Python 3.12 o una versión compatible con las dependencias.
- Git (solo si se desea clonar el repositorio).

### 1. Obtener el código

```bash
git clone https://github.com/TU-USUARIO/CRUD-MVC-Flask-SQLite.git
cd CRUD-MVC-Flask-SQLite
```

Sustituye `TU-USUARIO` por tu nombre de usuario de GitHub cuando publiques el repositorio. También puedes descargar el proyecto como ZIP.

### 2. Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 4. Ejecutar

```bash
python app.py
```

Abre en el navegador la dirección local que aparezca en la terminal; normalmente es `http://127.0.0.1:5000/login`.

### 5. Probar el sistema

1. Abre la pantalla de acceso y verifica el mensaje al usar credenciales incorrectas.
2. Inicia sesión con las credenciales de demostración configuradas en `controllers/auth_controller.py`.
3. Agrega un estudiante y comprueba que aparece en el listado.
4. Edita sus datos y verifica el cambio.
5. Elimina el registro y cierra sesión.

## Rutas principales

| Método | Ruta | Función |
| --- | --- | --- |
| GET, POST | `/login` | Mostrar y procesar inicio de sesión |
| GET | `/logout` | Cerrar sesión |
| GET | `/estudiantes` | Listar estudiantes |
| GET, POST | `/estudiantes/nuevo` | Crear estudiante |
| GET, POST | `/estudiantes/editar/<id>` | Editar estudiante |
| POST | `/estudiantes/eliminar/<id>` | Eliminar estudiante |

## Capturas de pantalla

Puedes añadir capturas de la versión final en una carpeta `docs/img/` y enlazarlas aquí:

```markdown
![Inicio de sesión](docs/img/login.png)
![Listado de estudiantes](docs/img/estudiantes.png)
```

## Consideraciones y mejoras futuras

- **Seguridad:** mover la clave secreta a una variable de entorno; sustituir las credenciales fijas por usuarios almacenados con contraseñas cifradas mediante hash.
- **Despliegue:** desactivar `debug=True` fuera del entorno de desarrollo y utilizar un servidor apropiado para producción.
- **Validaciones:** ampliar las comprobaciones de los formularios y gestionar registros inexistentes.
- **Funciones adicionales:** búsqueda, filtros, paginación y roles de usuario.

## Propósito académico

Este proyecto permite practicar rutas HTTP, formularios, sesiones, consultas SQL, plantillas HTML y separación de responsabilidades mediante MVC.
