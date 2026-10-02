from flask import Flask

app = Flask(__name__)

# o barra é o path, que é o caminho principal do site
@app.route('/')
def index():
    return 'Index Page'

# o barra hello, é outro caminho no site
@app.route('/hello')
def hello():
    return 'Hello, World'