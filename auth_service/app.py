from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='template')

users = {}
log_users = False

@app.route('/auth/signup', methods=['POST'])
def signup():
    global log_users
    if log_users:
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
    global log_users
    if log_users:
        return jsonify({"error": "User already logged in"}), 400
    data = request.get_json()
    if data['username'] not in users:
        return jsonify({"error": "User not found"}), 404
    elif users[data['username']] != data['password']:
        return jsonify({"error": "Invalid password"}), 401
    log_users = True
    return jsonify({"message": "User logged in"}), 200

@app.route('/auth/logout', methods=['POST'])
def logout():
    global log_users
    if not log_users:
        return jsonify({"error": "User not logged in"}), 400
    log_users = False
    return jsonify({"message": "User logged out"}), 200

@app.route('/auth/init')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)