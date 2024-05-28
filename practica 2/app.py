from flask import Flask,request

app = Flask(__name__)

#ruta
@app.route('/')
def principal():
    return 'Hola Mundo Flask'

#ruta doble
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Moi'


#ruta parametros
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola '+ nombre+'!!!'

#definicion de metodos de trabajo
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar pass por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para pass'

#manejo de excepciones
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontre nada'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
