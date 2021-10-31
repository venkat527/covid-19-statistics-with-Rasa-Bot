# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
import random
from datetime import date, datetime, timedelta
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionCovidStatus(Action):

    def name(self) -> Text:
        return "action_covid_status"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("##########")
        response = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        entities = tracker.latest_message['entities']
        print("Latest message now", entities)
        start_dt = date.today().replace(day=1, month=1).toordinal()
        end_dt = date.today().toordinal()
        rday = date.fromordinal(random.randint(start_dt, end_dt))
        print("random date",rday)
        edate = None
        state = None
        message = None
        print("before entity for loop")
        for e in entities:
            if e['entity'] == "GPE":
                state = e["value"]
                print("@@@state", state)
            if e['entity'] == "DATE":
                edate = e["value"]
                print("@@@edate", edate)
        print("after for loop")
        print("rtujkgd")
        for data in response["data"]:
             # print(data["day"])
             if data["day"] == edate:
                 print("@@@@main if@@")
                 total = data["summary"]["total"]
                 print("total cases in india on 2021-09-19 is ",total)
                 for region in data["regional"]:
                     #if region["loc"] == state.title():
                      if region["loc"] == state:
                          message = "Now Showing Cases For --> " + state.title() + "\n" + " \n" + "Confirmed: " + str(region["totalConfirmed"]) 
                              
                          #message = "Now Showing Cases For --> " + state.title() + " \n" + "Confirmed: " + region["totalConfirmed"]
                          print("confirmed cases in Delhi on 2021-09-19 is ",region["totalConfirmed"])
             elif data["day"] == str(rday): 
                 print("@@@elif@@@@")
                 total = data["summary"]["total"]
                 print(" r total cases in india on 2021-09-19 is ",total)
                 for region in data["regional"]:
                      #print(" region total cases in india on 2021-09-19 is ",total)
                      #if region["loc"] == state.title():
                      if region["loc"] == state:
                          print("inside regional if")
                          message = "Now Showing Cases For --> " + state.title() + "\n" + " \n" + "Confirmed: " + str(region["totalConfirmed"])
                          print("233",message)
                          #message = "Now Showing Cases For --> " + state.title() + "\n" + " \n" + "Confirmed: " + str(region["totalConfirmed"])
                           #message = "Now Showing Cases For --> " + state.title() + " \n" + "Confirmed: " + region["totalConfirmed"]
                          print("confirmed cases in Delhi on 2021-09-19 is ",region["totalConfirmed"])
             else:
                 message = "Could you please Rephrase it once again and please make sure that Date Format is 2021-06-25"

      
        print(message)
        dispatcher.utter_message(message)       
       # dispatcher.utter_message(text="Hello World!" + corono_status)

        return []
   