from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_api import status
from json import dumps
from flask import request
from flask import Response

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "admin": "root",
}



@app.route('/secret')
@auth.login_required
def secret_page():
    return Response("Hello, %s!" % auth.username(), 201, mimetype='application/json')

@app.route('/')
def root_test():
    return 'index'

@app.route('/user', methods=['GET'])
def get_users():
	return dumps(users)	

@app.route('/user/<string:username>', methods=['GET'])
def get_profile(username):
	return username + " profile"

@app.route('/user/<string:username>', methods=['POST'])
def add_user(username):
	users[username] = request.form['pwd']
	resp = Response(dumps(username), status=200, mimetype='application/json')
	return resp



if __name__ == '__main__':
    app.run()

