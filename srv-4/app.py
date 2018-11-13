from flask import Flask, jsonify
import os
import json
import requests
import random

nextServiceHost = os.getenv("NEXT_SERVICE","jsonplaceholderr.typicode.com")
nextServicePort = os.getenv("NEXT_SERVICE_PORT","443")
nextServiceRoute = os.getenv("NEXT_SERVICE_ROUTE","/users/")
app = Flask(__name__)

app_data = {'version': '2.1', 'name': 'service4', 'hostname': os.uname()[1], "status":"up" }

@app.route('/')
def default_root():
    rand_user = random.randint(1,10)
    nextService = "https://"+nextServiceHost+":"+nextServicePort+nextServiceRoute
    response = {app_data["name"]: app_data}
    
    returnedJson = {}

    try:
        r = requests.get(nextService+str(rand_user))
        returnedJson = r.json()
        app_data.update({"API_Data":returnedJson})

    except requests.exceptions.ConnectionError:
        app.logger.error("Error while connecting to %s", nextService)
        returnedJson = {nextService:{"status":"down"}}
        app_data.update(returnedJson)
    except json.decoder.JSONDecodeError:
        app.logger.error("Json parsing error!")
        returnedJson = {nextService:{"status":"down"}}
        app_data.update(returnedJson)


    return jsonify(response)