from flask import Flask, render_template, request, Response
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
@app.route('/envioformulario', methods=['POST'])
def envioformulario():
    print(request.form['nome'])
    print(request.form['telefone'])

    nome = request.form['nome']
    telefone = request.form['telefone']
    cpf = request.form['cpf']
    email = request.form['email']
    password = request.form['password']

    # validação no backend

    # salvar os dados no banco de dados
    # Connect to server
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin",
        database="formulario"
        )
    
    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SELECT CURDATE()")

    # Fetch one result
    row = cur.fetchone()
    print("Current date is: {0}".format(row[0]))

    sql = "INSERT INTO usuarios (nome, telefone, cpf, email, senha) VALUES (%s, %s, %s, %s, %s)"
    val = (nome, telefone, cpf, email, password)
    cur.execute(sql, val)

    cnx.commit()

    print(cur.rowcount, "record inserted.")

    return Response("Custom content", mimetype='text/plain', status=200)
if __name__ == '__main__':
    app.run(debug=True)