from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenar notas en memoria
notas = []

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    notas.append(data)
    return jsonify(data), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notas), 200

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    if id < len(notas):
        notas[id] = data
        return jsonify(notas[id]), 200
    return jsonify({"error": "Nota no encontrada"}), 404

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    if id < len(notas):
        nota = notas.pop(id)
        return jsonify(nota), 200
    return jsonify({"error": "Nota no encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)