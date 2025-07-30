from flask import Flask, request, jsonify
import jwt
import datetime
app = Flask(__name__)
SECRET_KEY = "mysecretkey"
USER_DATA = {
    "username": "raghav",
    "password": "11111"
}
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data['username'] == USER_DATA['username'] and data['password'] == USER_DATA['password']:
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
@app.route('/protected', methods=['GET'])
def protected():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Missing token"}), 401
    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({"message": "Token is valid", "user": decoded['user']})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
if __name__ == '__main__':
    app.run(debug=True)

