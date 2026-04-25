from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

if __name__ == '__main__':
    app.run(debug=True)