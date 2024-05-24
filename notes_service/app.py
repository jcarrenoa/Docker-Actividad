from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='template')

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
    global notas
    ids = int(id)
    i = 0
    if len(notas) > 0:
        for nota in notas:
            if ids == nota['id']:
                notas = notas.pop(i)
                return jsonify(notas), 200
    return jsonify({"error": "Nota no encontrada"}), 404

@app.route('/notes/init')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)