from flask import Flask, jsonify
from flask_cors import CORS
from tp import *

app = Flask(__name__)
CORS(app)  # Habilitar CORS

@app.route('/')
def home():
    return '<h1>Home</h1>'

@app.route('/<n_producto>', methods=['GET'])
def get_nivel(n_producto):
    datos = tp(n_producto)
    return jsonify(datos)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
