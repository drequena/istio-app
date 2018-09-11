from flask import Flask, jsonify
import os
import json
import requests

app = Flask(__name__)

app_data = {'version': '1.0', 'name': 'service1', 'hostname': os.uname()[1]}

@app.route('/')
def default_root():
    response = { app_data["name"]: app_data }

    r = requests.get("http://localhost:5001")

    response.update(r.json().items())
    
    return jsonify(response)
