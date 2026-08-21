from flask import Flask

app = Flask(__name__)

# o barra é o path, que é o caminho principal do site
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"