from flask import Flask, render_template, request, Response

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

    // proximas aulas...

    // validação no backend

    // salvar os dados no banco de dados

    return Response("Custom content", mimetype='text/plain', status=200)
if __name__ == '__main__':
    app.run(debug=True)