from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User signed up"}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    # Aquí puedes agregar la lógica de autenticación
    return jsonify({"message": "User logged in"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)