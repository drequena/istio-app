from flask import Flask, jsonify
import os
import json
import requests

nextServiceHost = os.getenv("NEXT_SERVICE","localhost")
nextServicePort = os.getenv("NEXT_SERVICE_PORT","5001")
nextService = "http://"+nextServiceHost+":"+nextServicePort
app = Flask(__name__)

app_data = {'version': '1.0', 'name': 'service1', 'hostname': os.uname()[1], "status":"up"}

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