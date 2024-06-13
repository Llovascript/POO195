from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('home.html')

# ruta del formulario
@app.route('/formulario')
def formulario():
    return render_template('index.html')

# forms
@app.route('/form_submit', methods=['POST'])
def form_submit():
    if request.method == 'POST':
        Nombre = request.form['txtNombre']
        Edad = request.form['txtEdad']
        print(Nombre, Edad)
        return 'Datos recibidos en el servidor'

# numero al cuadrado
@app.route("/cuadrado/<int:num>")
def cuadrado(num):
    return f'El cuadrado de {num} es: {num**2}'

# Error 404
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontre nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True)