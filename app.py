from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hey... Don't worry, be happy!"

if __name__ == '__main__':
    app.run(debug=True)