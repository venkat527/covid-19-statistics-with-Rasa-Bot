# covid-19-statistics-with-Rasa-Bot
This bot will give covid-19 statistics like covid status in india using covid-19 india stats root history [api](https://api.rootnet.in/covid19-in/stats/history)
## How To Run Bot
#### Prerequisite:
* rasa
* python 3.7.2
* spacy
* en_core_web_sm spacy model
### Steps To chat with bot in CMD
1. open CMD in project path and enter below command to run Action Server

**rasa run actions**

2. open Another CMD in project path and enter below command to run rasa server

**rasa shell**

### Steps to Run with Flask App
1. open CMD and navigate to actions folder and run flask server 
2. open CMD in project path and enter below command to run Action Server

**rasa run actions**

3. open flask url in browser then you are able to chat with Bot

#### How To chat with only NLU Model 
 * By using rasa shell nlu command we can chat with nlu model
 * NLU Model will give response as Entity's, slots and intent rankings
 * Based on intent rankings core model will select highest threshold value intent 
 * finally Core model will give response to the user question based on utter  

### Justifications And Findings


1. SpacyNLP
   spacy model will extract names,cities,Locations 
2. Duckling server 
   Duckling is Haskel Library introduced by wit.ai
   Duckling is also used to extract Entities, Date,Time from text
#### How To Dockerize Bot Application
we have three options to dockerize bot application
1. one-line deploy script
2. Kubernetes/Openshift
3. Docker Compose

#### My Road Blocks:

* i have faced machine compatibility issues while working with rasa i.e tensorflow lack of machine that's my bad.
* unable to start duckling server in windows, this duckling library is used to improve model accuracy.



