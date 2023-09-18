# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/ping")
def ping():
    print("❇️ Received GET request to /api/ping")
    response = jsonify(message='pong!!!')
    response.headers.add('Access-Control-Allow-Origin','*')  # Allow requests from any origin
    return response

if __name__ == '__main__':
    port = 3000
    print("❇️ Ask Piles Flask API is listening on port {}".format(port))
    app.run(port=port)
