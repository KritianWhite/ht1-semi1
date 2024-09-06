# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: /check
@app.route('/check', methods=['GET'])
def check_status():
    return "Status: OK", 200

# Endpoint 2: /
@app.route('/', methods=['GET'])
def get_data():
    data = {
        "Instancia": 'Instancia #2 - API 2',
        "Curso": 'Seminario de Sistemas 1',
        "Seccion": 'Seccion A',
        "Periodo": '2do Semestre 2024',
        "Estudiante": 'Christian Blanco - 202000173',
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
