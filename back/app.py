from flask import Flask, jsonify
from flask_cors import CORS
from tp import *

app = Flask(__name__)
CORS(app)  # Habilitar CORS

@app.route('/')
def home():
    return '<h1>Home</h1>'

@app.route('/<costo_producto>/<valor_recupero>/<cantidad_dias>/<tamano_lote>/<stock_inicial>', methods=['GET'])
def get_nivel(costo_producto, valor_recupero, cantidad_dias, tamano_lote, stock_inicial):
    datos = tp(costo_producto, valor_recupero, cantidad_dias, tamano_lote, stock_inicial)
    return jsonify(datos)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
