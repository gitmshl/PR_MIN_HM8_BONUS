from flask import Flask, url_for, request, jsonify
from markupsafe import escape
import requests

app = Flask(__name__)

def server_num(filename):
    return 1 + (len(filename) % 2)


@app.route('/<filename>', methods=['GET'])
def get(filename):
    port = 8080 if server_num(filename) == 1 else 8081
    r = requests.get(f"http://localhost:{port}/storage/{filename}")
    return r.text, r.status_code

@app.route('/<filename>', methods=['PUT'])
def put(filename):
    port = 8080 if server_num(filename) == 1 else 8081
    data1 = request.json
    print(f"DATA: {data1}")
    print(type(data1))
    r = requests.put(f"http://localhost:{port}/storage/{filename}", data=str(data1))
    return r.text, r.status_code


@app.route('/<filename>', methods=['DELETE'])
def profile(filename):
    port = 8080 if server_num(filename) == 1 else 8081
    r = requests.delete(f"http://localhost:{port}/storage/{filename}")
    return r.text, r.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8082')
