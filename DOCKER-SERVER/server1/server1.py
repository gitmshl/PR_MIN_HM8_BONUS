from flask import Flask, url_for, request, jsonify
from markupsafe import escape

app = Flask(__name__)

files = {}

@app.route('/storage/<filename>', methods=['GET'])
def get(filename):
    global files
    if filename in files:
        return files[filename], 200
    return "", 404

@app.route('/storage/<filename>', methods=['PUT'])
def put(filename):
    global files
    data = request.json
    files[filename] = data
    return "", 201

@app.route('/storage/<filename>', methods=['DELETE'])
def profile(filename):
    global files
    if filename in files:
        del files[filename]

    return "", 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
