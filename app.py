import os
from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Heros World!"

@app.route('/heros.json')
def cities():
    data = ['Ironman', 'captain america', 'Black panter', 'Captain marvel']
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
