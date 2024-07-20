from flask import Flask,request, render_template,url_for,redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mediclin'

app.secret_key='mysecretkey'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/RegistroM")
def RegistroM():
    return render_template('Registro.html')

@app.route("/guardarMedico", methods=["POST"])
def guardarMedico():
    if request.method == 'POST':
        #tomamos los datos que vienen por post
        FRFCc = request.form['txtRFC']
        FNombre = request.form['txtNombre']
        FCedula = request.form['txtCedula']
        FCorreo = request.form['txtCorreo']
        FPassword = request.form['txtPassword']
        FRol = request.form['txtRol']
        FCons = request.form['txtconsultorio']
        
        
        cursor = mysql.connection.cursor()
        cursor.execute('insert into medico(RFC,Nombre,Cedula,Correo,Password,Rol,consultorio) values(%s,%s,%s,%s,%s,%s,%s)', (FRFCc, FNombre, FCedula,FCorreo,FPassword,FRol,FCons))
        mysql.connection.commit()
        
        flash('Album guardado exitosamente')
        
        return redirect(url_for('listaUsuarios')) 
        
@app.route("/listaUsuarios")
def listaUsuarios():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT idMedico, RFC, Nombre, Cedula, Correo, Rol, consultorio FROM medico')
    consulta = cursor.fetchall()
    return render_template('consulta.html', usuarios=consulta)


@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontre nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
