from flask import Flask, url_for, request, jsonify
from markupsafe import escape
import json

app = Flask(__name__)

files = {}

@app.route('/storage/<filename>', methods=['GET'])
def get(filename):
    global files
    print(files)
    if filename in files:
        return files[filename], 200
    return "", 404

@app.route('/storage/<filename>', methods=['PUT'])
def put(filename):
    global files
    data = json.loads(request.data.decode('utf-8').replace("'", '"'))
    print(f"data: {data}")
    print(type(data))
    files[filename] = data
    return "", 201

@app.route('/storage/<filename>', methods=['DELETE'])
def profile(filename):
    global files
    if filename in files:
        del files[filename]

    return "", 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8081')
