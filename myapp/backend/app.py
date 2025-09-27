from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return jsonify({"message": "Hello from Backend!"})

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json() or {}
    result = data.get("a", 0) + data.get("b", 0)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
