from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
loged_users = False

@app.route('/auth/signup', methods=['POST'])
def signup():
    global loged_users
    if loged_users:
        return jsonify({"error": "User already logged in"}), 400
    data = request.get_json()
    if data['username'] in users:
        return jsonify({"error": "User already exists"}), 400
    else:
        users[data['username']] = data['password']
    return jsonify({"message": "User signed up"}), 201

@app.route('/auth/signup', methods=['GET'])
def get_signup():
    return jsonify(users), 200

@app.route('/auth/login', methods=['POST'])
def login():
    global loged_users
    if loged_users:
        return jsonify({"error": "User already logged in"}), 400
    data = request.get_json()
    if data['username'] not in users:
        return jsonify({"error": "User not found"}), 404
    elif users[data['username']] != data['password']:
        return jsonify({"error": "Invalid password"}), 401
    loged_users = True
    return jsonify({"message": "User logged in"}), 200

@app.route('/auth/logout', methods=['POST'])
def logout():
    global loged_users
    if not loged_users:
        return jsonify({"error": "User not logged in"}), 400
    loged_users = False
    return jsonify({"message": "User logged out"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)