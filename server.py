import math
import flask
from flask import jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return flask.send_file('index.html')

@app.route('/test/<command>')
def test(command):
  # check this out, match!
  # https://peps.python.org/pep-0636/
  match command.split('-'):
    case ['add', a, b]:
      return str(int(a) + int(b))
    case ['multiply', a, b]:
      return str(int(a) * int(b))
    case ['ln', x]:
      return str(math.log(float(x)))
    case _:
      flask.abort(400)
      
@app.route("/api/ping")
def ping():
    print("❇️ Received GET request to /api/ping")
    response = jsonify(message='pong!!!')
    response.headers.add('Access-Control-Allow-Origin','*')  # Allow requests from any origin
    return response

if __name__ == '__main__':
    print("❇️ Ask Piles Flask API is listening")

