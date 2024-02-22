from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta principal para mostrar la lista de estudiantes
@app.route('/')
def index():
    # Conectar a la base de datos (creará el archivo si no existe)
    conexion = sqlite3.connect('estudiantes.db')
    cursor = conexion.cursor()

    # Ejecutar una consulta para obtener todos los estudiantes
    cursor.execute("SELECT Numpliza, Nombreasegurado, Identificacion, Vigdesde, Vighasta, Participa FROM estudiantes")
    estudiantes = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    # Renderizar la plantilla HTML con la lista de estudiantes
    return render_template('index.html', estudiantes=estudiantes)

# Ruta para agregar un nuevo estudiante
@app.route('/agregar_estudiante', methods=['POST'])
def agregar_estudiante():
    if request.method == 'POST':
        Numpliza = request.form['pliza']
        Nombreasegurado = request.form['nombre asegurado']
        Identificacion = request.form['cedula']
        Vigdesde = request.form['fecha inicial']
        Vighasta = request.form['fecha fianl']
        Participa = request.form['si o no']

        # Conectar a la base de datos
        conexion = sqlite3.connect('estudiantes.db')
        cursor = conexion.cursor()

        # Insertar el nuevo estudiante en la base de datos
        cursor.execute("INSERT INTO estudiantes (Numpliza, Nombreasegurado, Identificacion, Vigdesde, Vighasta, Participa) VALUES (?, ?, ?, ?, ?, ?)", 
                        (Numpliza, Nombreasegurado, Identificacion, Vigdesde, Vighasta, Participa ))

        # Guardar los cambios
        conexion.commit()

        # Cerrar la conexión
        conexion.close()

        # Redirigir a la página principal después de agregar el estudiante
        return redirect(url_for('index'))

# Punto de entrada del programa
if __name__ == '__main__':
    # Iniciar la aplicación Flask
    app.run(debug=True)
