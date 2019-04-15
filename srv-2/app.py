from flask import Flask, jsonify
import os
import json
import requests
from time import sleep

envSleepTime = os.getenv("SLEEP_TIME","0.0")
nextServiceHost = os.getenv("NEXT_SERVICE","localhost")
nextServicePort = os.getenv("NEXT_SERVICE_PORT","5002")
nextService = "http://"+nextServiceHost+":"+nextServicePort
app = Flask(__name__)

app_data = {'version': '2.0', 'name': 'service2', 'hostname': os.uname()[1], "status":"up"}

try:
    sleepTime = float(envSleepTime)
except:
    app.logger.error("ENV SLEEP_TIME to float error! Switching to default 0.0s")
    sleepTime = 0.0

@app.route('/')
def default_root():
    response = { app_data["name"]: app_data }
    
    returnedJson = {}

    try:
        r = requests.get(nextService)
        returnedJson = r.json()
    except requests.exceptions.ConnectionError:
        app.logger.error("Error while connecting to %s", nextService)
        returnedJson = {nextService:{"status":"down"}}
    except json.decoder.JSONDecodeError:
        app.logger.error("Json parsing error!")
        returnedJson = {nextService:{"status":"down"}}

    response.update(returnedJson.items())

    sleep(sleepTime)
    return jsonify(response)
