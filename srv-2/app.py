from flask import Flask, jsonify
import os
import json
import requests

app = Flask(__name__)

app_data = {'version': '1.7', 'name': 'service2', 'hostname': os.uname()[1]}

@app.route('/')
def default_root():
    response = { app_data["name"]: app_data }

    r = requests.get("http://localhost:5002")

    response.update(r.json().items())

    return jsonify(response)
