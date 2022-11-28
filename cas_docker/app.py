"""
@author: Mehdi

Projet web S7 - Python API CaS
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from jwt import encode
import json
import datetime
#import mysql.connector as MC
import random
import string

app = Flask(__name__)
CORS(app)

database = {"logs": ["fabien","maxence","salah"],"roles": ["admin","lecteur","superviseur"]}

@app.route('/login', methods=['POST'])
def getToken():
    if request.is_json:
        data_request = request.get_json(silent=True)

        userCas = data_request.get('user')
        passwordUser = data_request.get('password')

        if(getRoles(passwordUser)!= None ):
            token = create_token()
            roles = getRoles(passwordUser)
            return {'roles': roles, 'token': token}
        else:
            return {'error': 'Bad credentials'}, 401
    else:
        return {'error': 'Request must be JSON'}, 400



def getRoles(password):
    database = {'jung':'admin','sadou':'superviseur','dieuducas':'lecteur'}
    data = database.get(password)
    return data

"""def databaseResponse(user,password):


    try:
        conn = MC.connect(user ='student', password ='password',host='localhost', database = 'utilisateurs')
        cursor = conn.cursor()

        req = 'SELECT roles FROM users WHERE logs = ' + '\"'+user+'\" AND password = '+'\"'+password+'\"'
        cursor.execute(req)

        response = cursor.fetchone()
        return response[0]

    except MC.Error as err :
        print(err)

    finally :
        if(conn.is_connected()):
            cursor.close()
            conn.close()
"""
def create_token():
    encoded = encode({"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=10)}, "D3s0l3/d3Nv0yER-1ePr0Jet_4uS51tARd", algorithm="HS256")
    return str(encoded)


'''if __name__ == '__main__':
    app.run(debug=True)
    print("api running")'''