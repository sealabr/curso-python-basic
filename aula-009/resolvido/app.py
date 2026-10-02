from flask import Flask, render_template, request, Response, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')
@app.route('/editar')
def editar():
    return render_template('editar.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')
@app.route('/consultaformulario')
def consultaformulario():
    return render_template('consultaformulario.html')
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

@app.route('/alteraformulario', methods=['POST'])
def alteraformulario():

    meuid = request.form['id']
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

    sql = "UPDATE usuarios SET nome = '%s', telefone = %s, cpf = '%s', email = '%s', senha = '%s' WHERE id = %s"
    cur.execute(sql % (nome, telefone, cpf, email, password, meuid))

    cnx.commit()

    print(cur.rowcount, "record altered!")

    return Response("Custom content", mimetype='text/plain', status=200)


@app.route('/getformulario')
def getformulario():
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
    cur.execute("SELECT * FROM usuarios")

    # 2. Fetch all rows
    rows = cur.fetchall()

    # 1. Cria uma lista vazia para guardar os resultados
    all_results = []

    # 2. Passa por cada linha retornada do banco de dados
    for row in rows:
        usuario = {
            "id": row[0],
            "nome": row[1],
            "telefone": row[2],
            "cpf": row[3],
            "email": row[4]
        }
        
        # Adicionamos esse dicionário na nossa lista principal
        all_results.append(usuario)

    # Transforma a lista de dicionários em uma string JSON formatada
    return jsonify(all_results)

@app.route('/getregistro')
def getregistro():
    # Connect to server
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="admin",
        database="formulario"
        )

    # pega o id do parametro da url
    id = request.args.get('id')

    # Get a cursor
    cur = cnx.cursor()

    # Execute a query passando o id de parametro
    sql = "SELECT * FROM usuarios WHERE id = %s"
    cur.execute(sql % (id))

    # traz um registro
    row = cur.fetchone()

    usuario = {
        "id": row[0],
        "nome": row[1],
        "telefone": row[2],
        "cpf": row[3],
        "email": row[4]
    }

    return jsonify(usuario)

if __name__ == '__main__':
    app.run(debug=True)