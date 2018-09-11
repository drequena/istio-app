from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

app_data = {'version': '1.2', 'name': 'service3', 'hostname': os.uname()[1]}

@app.route('/')
def default_root():
    return jsonify({app_data["name"]:app_data})
