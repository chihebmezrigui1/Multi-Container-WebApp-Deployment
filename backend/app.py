import time
import math
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/write/<data>", methods=["POST"])
def write_data(data):
    with open("/data/log.txt", "a") as file:
        file.write(f"{data}\n")
    return jsonify(message="Data written successfully"), 200

@app.route("/read", methods=["GET"])
def read_data():
    with open("/data/log.txt", "r") as file:
        log_data = file.readlines()
    return jsonify(data=log_data), 200

@app.route("/compute", methods=["GET"])
def compute():
    start_time = time.time()
    result = 0
    for i in range(1, 10000000):
        result += math.sin(i) * math.cos(i)
    end_time = time.time()
    execution_time = end_time - start_time
    return jsonify(result=result, execution_time=f"{execution_time:.2f} seconds"), 200

@app.route("/status", methods=["GET"])
def status():
    return jsonify(status="Backend is running"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3402)
