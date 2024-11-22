from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:3402"  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/write", methods=["POST"])
def write():
    data = request.form["data"]
    response = requests.post(f"{BACKEND_URL}/write/{data}")
    return jsonify(response.json())

@app.route("/read", methods=["GET"])
def read():
    response = requests.get(f"{BACKEND_URL}/read")
    return jsonify(response.json())

@app.route("/compute", methods=["GET"])
def compute():
    response = requests.get(f"{BACKEND_URL}/compute")
    return jsonify(response.json())

@app.route("/status", methods=["GET"])
def status():
    response = requests.get(f"{BACKEND_URL}/status")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3403)
