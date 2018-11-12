from flask import Flask, jsonify
import os
import json
import requests

nextServiceHost = os.getenv("NEXT_SERVICE","jsonplaceholder.typicode.com")
nextServicePort = os.getenv("NEXT_SERVICE_PORT","443")
nextServiceRoute = os.getenv("NEXT_SERVICE_ROUTE","/users/1")
nextService = "https://"+nextServiceHost+":"+nextServicePort+nextServiceRoute
app = Flask(__name__)

app_data = {'version': '2.1', 'name': 'service4', 'hostname': os.uname()[1], "status":"up"}

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

    return jsonify(response)
