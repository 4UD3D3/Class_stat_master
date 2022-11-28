# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:38:45 2022

@author: grego

Script to extract all statistics from ics file and convert it to json file (python dictionnary)
"""
from icalendar import Calendar
#import argparse
from dataclasses import dataclass
import datetime

@dataclass
class Creneau:
    """Classe représentant un créneau, avec une heure de départ et de fin."""
    start: datetime.time
    end: datetime.time

creneau_list = {'C1_8h00-9h30': Creneau(datetime.time(8,0),datetime.time(9,30)),
                'C2_9h45-11h15': Creneau(datetime.time(9,45),datetime.time(11,15)),
                'C3_11h30-13h00': Creneau(datetime.time(11,30),datetime.time(13,0)),
                'C4_13h00-14h30': Creneau(datetime.time(13,0),datetime.time(14,30)),
                'C5_14h45-16h15': Creneau(datetime.time(14,45),datetime.time(16,15)),
                'C6_16h30-18h00': Creneau(datetime.time(16,30),datetime.time(18,00)),
                'C7_18h15-19h45': Creneau(datetime.time(18,15),datetime.time(19,45))
                }

weekday = { '1': "D1_Lundi",
            '2': "D2_Mardi",
            '3': "D3_Mercredi",
            '4': "D4_Jeudi",
            '5': "D5_Vendredi",
            '6': "D6_Samedi",
            '7': "D7_Dimanche"
            }

Empty_day_count = {'C1_8h00-9h30': 0,
                   'C2_9h45-11h15': 0,
                   'C3_11h30-13h00': 0,
                   'C4_13h00-14h30': 0,
                   'C5_14h45-16h15': 0,
                   'C6_16h30-18h00': 0,
                   'C7_18h15-19h45': 0
                   }

def getEmptyRoomList():
    return {'C1_8h00-9h30': list(),
            'C2_9h45-11h15': list(),
            'C3_11h30-13h00': list(),
            'C4_13h00-14h30': list(),
            'C5_14h45-16h15': list(),
            'C6_16h30-18h00': list(),
            'C7_18h15-19h45': list()
            }

def getEmptyJSON(DTSTART: datetime.date,DTEND: datetime.date):
    """
    DTSTART: Date start where first event can occur
    DTEND: Last date where event can occur
    Return empty Json to start counting class occupation and class concerned
    """
    room_count = dict()
    room_list = dict()
    
    #Add each day to dict
    date_to_process = DTSTART
    while(date_to_process <= DTEND):
        infos_date = date_to_process.isocalendar()
        year = str(infos_date[0])
        week = str(infos_date[1])
        day = weekday[str(infos_date[2])]
        
        #On ne prend pas en compte le week end
        if day == "D7_Dimanche":
            date_to_process += datetime.timedelta(days=1)
            continue
        
        #Year
        if room_count.get(year) == None:
            room_count[year] = dict()
            room_list[year] = dict()
            
        #Week
        if room_count[year].get(week) == None:
            room_count[year][week] = dict()
            room_list[year][week] = dict()
        
        #Day
        room_count[year][week][day] = Empty_day_count.copy()
        room_list[year][week][day] = getEmptyRoomList()
        
        #Increment day
        date_to_process += datetime.timedelta(days=1)
    
    return room_count, room_list

def estEntre(value_test, low, high):
    """
    Renvoie TRUE si value_test se trouve entre low et high
    """
    return value_test>low and value_test<high

#Return true si le cours se déroule sur le créneau avec les horaires spécifiées
def isRoomOccupiedOnCreneau(start_cours, end_cours, start_creneau, end_creneau):
    if estEntre(start_cours, start_creneau, end_creneau) or estEntre(end_cours, start_creneau, end_creneau):
        return True
    if start_cours <= start_creneau and end_cours > start_creneau:
        return True
    return False

def getCreneauFromPeriod(DTSTART,DTEND):
    """
    Parameters
    ----------
    DTSTART : Starting date and time of the event
    DTEND : Ending date and time of the event

    Returns
    -------
    Une liste des créneaux occupés en fonction des horaires passés en paramètre (on ne
    s'intéresse qu'aux heures de la journée dans ce cas)

    """
    start_time = DTSTART.time()
    end_time = DTEND.time()
    
    list_creneau_occupes = list()
    
    for creneau in creneau_list.keys():
        c_start = creneau_list[creneau].start
        c_end = creneau_list[creneau].end
        
        #Verify if the event occur on this creneau
        if isRoomOccupiedOnCreneau(start_time, end_time, c_start, c_end):
            list_creneau_occupes.append(creneau)
            
    return list_creneau_occupes

def addEventStat(list_creneaux, room, day:datetime, rooms_count, rooms_list):
    event_day = day.isocalendar()
    year = str(event_day[0])
    week = str(event_day[1])
    day = weekday[str(event_day[2])]
    
    for creneau in list_creneaux:
        #On vérifie que la salle n'est pas déjà référencée
        if room not in rooms_list[year][week][day][creneau]:
            rooms_count[year][week][day][creneau] +=1
            rooms_list[year][week][day][creneau].append(room)

def getStatsFromICS(ics_file, date_start, date_end, room_list):
    """

    Parameters
    ----------
    ics_file : opened ics_file to read from
    date_start : Date on which the events to be analyzed begin
    date_end : date on which the events to be analyzed end
    room_list : All rooms to analyse

    Returns
    -------
    Read event from ics file and add statistic (related to each event) in the dictionnary

    """
    #Reading input file as an ics file
    calendar = Calendar.from_ical(ics_file.read())
    
    #Initialise empty JSON for count and room list
    rooms_count, rooms_list = getEmptyJSON(date_start, date_end)

    for component in calendar.walk():
        if component.name == "VEVENT":
            #On récupère les informations sur le cours
            rooms_event = component.get('location').split(',')
            
            for room in rooms_event:
                if room not in room_list:
                    continue
                
                start_event = component.get('dtstart').dt
                end_event = component.get('dtend').dt
                
                #On détermine les créneaux occupés pour cette salle et mettons à jour les dictionnaires en conséquence
                creneaux_occupes = getCreneauFromPeriod(start_event, end_event)
                addEventStat(creneaux_occupes, room, start_event, rooms_count, rooms_list)
                
    #Une fois tous les évènements du fichier ics considérés on retourne les fichiers stats à jour
    return rooms_count, rooms_list

"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract all rooms from an ics file.')
    parser.add_argument("-i", "--input", required=True,
                        help="Path to the calendar file.")

    args = parser.parse_args()

    main(args)
"""
