# -*- coding: utf-8 -*-
"""
@author: grego, auDede, Mehdi

Projet web S7 - Python API to get data from Ics files (+ CAS Provisoirement)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from extract_stats_ics_to_json import getStatsFromICS, getEmptyJSON
from base64 import b64decode as mypersonaldecode
import datetime
import smtplib, ssl
import LaRedemption
import os
import requests
from datetime import date, timedelta
import json
from jwt import encode
import json
import datetime
#import mysql.connector as MC
import random
import string


app = Flask(__name__)
CORS(app)
reponse=""

class Mail:
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "classstat.ensibs@gmail.com"
        self.pswd='cGFqY2JnaGd3ZHlpa3d1bQ=='


    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, mypersonaldecode(self.pswd).decode("utf-8"))

        for email in emails:#send the mail with the content
            service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

class Creneau:
    def __init__(self, year, week, day, time):
        self.annee = year
        self.semaine = week
        self.jour = day
        self.creneau = time
    
    def retour(self):
        return (f"Annee = {self.annee}, semaine = {self.semaine}, jour = {self.jour}, creneau = {self.creneau}\n")



def alerte():
    today = date.today()
    nextWeek = today + timedelta(days=3)
    d1 = today.strftime("%Y%m%d") #today 
    d2 = nextWeek.strftime("%Y%m%d")    #in 1 week
    tabCreneauFull = []
    with open('data/out','r') as myFile:#build json for request
        tab = []
        for ligne in myFile: #create a tab of all rooms
            tab.append(ligne.split("\n")[0])
    myjson = { #json to send
        'start_date':d1,
        'end_date':d2,
        'rooms_list':tab}
    x = requests.post("http://127.0.0.1:5000/data", json = myjson) #request to have the json with the data of the room that we want
    json_response = json.loads(x.content.decode('utf8')) 
    for element_dict in json_response:
        for annee in element_dict.keys():
            for semaine in element_dict[annee].keys():
                for jour in element_dict[annee][semaine].keys():
                    for creneau in element_dict[annee][semaine][jour].keys():
                        if not isinstance(element_dict[annee][semaine][jour][creneau], int) and len(element_dict[annee][semaine][jour][creneau]) > int(0.4*len(tab)): #si il y a plus de 90% des salle de remplie
                            tabCreneauFull.append(Creneau(annee,semaine,jour,creneau)) 
    returnthings = ""
    for things in tabCreneauFull:
        returnthings += things.retour() #create the string to send by mail in the good format
    return returnthings




# http://127.0.0.1:5000/add_email and send somthing like : {"email" : "test2@gmail.com"}
@app.route('/add_email', methods=['POST'])
def add_email():
    if request.is_json:
        req = request.get_json()
        with open('data/botmail.conf', 'a') as input:
            print(req)
            try:
                input.write(req['email'] + '\n')
            except IOError:
                print('no email argument in json object')
                return {'error': 'Request \"email\" flasg in the json'}, 400

        return jsonify(req), 201
    else:
        return {'error': 'Request must be JSON'}, 400


@app.route('/del_email', methods=['POST'])
def delemail():
    if request.is_json:
        req = request.get_json()
        with open('data/botmail.conf', 'r') as input:
            with open('data/botmail.conf.temp', 'w') as output :
                for ligne in input:
                    if req['email'] not in ligne:
                        output.write(ligne)
        os.remove('data/botmail.conf')
        os.rename('data/botmail.conf.temp', 'data/botmail.conf')
        return jsonify(req), 201
    else:
        return {'error': 'Request must be JSON'}, 400



@app.route('/send_alert', methods=['GET'])
def sendAlerte():    
    try:
        with open('data/icsfileall.ics'):
            pass
    except IOError:
        LaRedemption.loadICSFile()
    themailcontent = alerte()
    with open('data/botmail.conf', 'r') as emaillist:
        mail = Mail()
        mail.send(emaillist, "Class Stat Alert !", themailcontent)
    return themailcontent, 200


"""
Request for json data from ICS files must be sent to /data with post request
With following parameters class_names, start_date and end_date in json

Following parameters should be sent with post request
rooms_list : ["room1","room2"...] -> List of all class to analyse
start_date : aaaammdd -> Starting date to retrieve stats
end_date : aaaammdd -> End date to retrieve stats
"""
@app.route('/data', methods=['POST'])
def getDataFromClass():
    #Retrieve json from post method
    data_request = request.get_json(silent=True)
    
    #Parse parameters from json request
    room_list = data_request.get('rooms_list')
    start_date = getDatetimeFromDate(data_request.get('start_date'))
    end_date = getDatetimeFromDate(data_request.get('end_date'))
    
    #Get ICS file for each room and analyse them
    ics_generated = LaRedemption.getICSFile(start_date, end_date, room_list, 1)
        
    if ics_generated != None:
        rooms_count, rooms_list = getStatsFromICS(ics_generated, start_date, end_date, room_list)
        ics_generated.close()
    
    else:
        print("Fichier ics non récupéré pour les salles sélectionnées")
    
    #On renvoie les statistiques sous formes JSON
    return [rooms_count, rooms_list]
    
"""
Returns the datetime.date format corresponding do the date with format aaaammdd
"""
def getDatetimeFromDate(simple_date):
    if(len(simple_date) != 8):
        return None
    
    year = int(simple_date[:4])
    month = int(simple_date[4:6])
    day = int(simple_date[6:8])
    return datetime.date(year,month,day)


"""
//////////////////
PARTIE CAS Provisoirement
//////////////////
"""

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

def create_token():
    encoded = encode({"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)}, "D3s0l3/d3Nv0yER-1ePr0Jet_4uS51tARd", algorithm="HS256")
    return str(encoded)