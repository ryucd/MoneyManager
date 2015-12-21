import os
from bottle import get, post, request, route, run, view
from oauth2client import client, crypt

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

def verifyToken(token):
	try:
		idinfo = client.verify_id_token(token, CLIENT_ID)
		if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
			raise crypt.AppIdentityError("Wrong issuer.")
	except crypt.AppIdentityError:
		#Invalid token
		return False
	userid = idinfo['sub']
	return True

@post("/tokensignin")
def tokenSignin():
	token = request.forms.get('idtoken')
	if verifyToken(token) == False:
		return "Bad Access"
	else:
		return "Success"

@route("/")
@view("view/signin")
def hello_world():
	return dict(title="title")

run(host="localhost", port=int(os.environ.get("PORT", 8080)))
