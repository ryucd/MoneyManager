import os
from bottle import get, post, request, route, run, view, template
from oauth2client import client, crypt

import db

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

@route("/app")
def app_index():
    money = {"name":"Title", "amount":100, "date":"15/12/22"}
    datalist = [money, money]
    return template("view/index", datalist=datalist)

@route("/")
def hello_world():
    return template("view/signin", dict(title="title", GOOGLE_CLIENT_ID=CLIENT_ID, SERVER_URL=os.getenv("SERVER_URL")))

run(host=os.getenv("HOST_NAME"), port=int(os.environ.get("PORT", 8080)))
