from flask import Flask, jsonify
import os
import json
import mysql.connector
import requests

databasehost = os.getenv("DATABASEHOST","localhost")
databaseuser = os.getenv("DATABASEUSER","root")
databasepass = os.getenv("DATABASEPASS","123456")
databasename = os.getenv("DATABASENAME","data")
databaseport = os.getenv("DATABASEPORT","3306")

nextServiceHost = os.getenv("NEXT_SERVICE","localhost")
nextServicePort = os.getenv("NEXT_SERVICE_PORT","5003")
nextService = "http://"+nextServiceHost+":"+nextServicePort

app = Flask(__name__)

app_data = {'version': '1.2', 'name': 'service3', 'hostname': os.uname()[1], "status":"up"}

@app.route('/')
def default_root():
    response = { app_data["name"]: app_data }

    returnedJson = {}

    try:
        mydb = mysql.connector.connect(host=databasehost,port=databaseport,user=databaseuser,passwd=databasepass,database=databasename)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tv_show ORDER BY RAND() LIMIT 1;")
        myresult = mycursor.fetchone()
        mycursor.close()
        mydb.close()

        result={"db_data":{"id":myresult[0],"name":myresult[1],"score":myresult[2],"year":myresult[3]}}

        app_data.update(result.items())

        r = requests.get(nextService)
        returnedJson = r.json()

        app_data.update(result.items())
        app_data.update(returnedJson.items())

    except requests.exceptions.ConnectionError:
        app.logger.error("Error while connecting to %s", nextService)
        returnedJson = {nextService:{"status":"down"}}
    except:
        app_data.update({"db_data":"Failed to connect to DB"})
        app.logger.error("Failed to connect to DB")
    
    return jsonify(response)
