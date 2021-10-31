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
        
        response = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
        entities = tracker.latest_message['entities']
        start_dt = date.today().replace(day=1, month=1).toordinal()
        end_dt = date.today().toordinal()
        rday = date.fromordinal(random.randint(start_dt, end_dt))
        edate = None
        state = None
        message = None
        for e in entities:
            if e['entity'] == "GPE":
                state = e["value"]
            if e['entity'] == "DATE":
                edate = e["value"]
        for data in response["data"]:
             if data["day"] == edate:
                 total = data["summary"]["total"]
                 for region in data["regional"]:
                      if region["loc"] == state:
                          message = "Now Showing covid-19 india statistics For --> " + state.title() + "\n" + " \n" + "Confirmed: " + str(region["totalConfirmed"] + " \n" + "Recovered: " + str(region["discharged"] + " \n" + "deaths: " + str(region["deaths"])             
             elif data["day"] == str(rday): 
                 total = data["summary"]["total"]
                 for region in data["regional"]:
                      if region["loc"] == state:
                          message = "Now Showing covid-19 india statistics For --> " + state.title() + "\n" + " \n" + "Confirmed: " + str(region["totalConfirmed"] + " \n" + "Recovered: " + str(region["discharged"] + " \n" + "deaths: " + str(region["deaths"])
                          
                          
             else:
                 message = "Could you please Rephrase it once again and please make sure that Date Format is 2021-06-25"

      
        print(message)
        dispatcher.utter_message(message)       
       
        return []
   