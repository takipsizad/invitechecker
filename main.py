import flask
from flask import request
from flask import Flask
from threading import Thread
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Response
import os
import json

load_dotenv()

app = Flask("")
client = MongoClient(os.getenv("db"))
mydb = client["db"]
blacklist = mydb.blacklist


@app.route("/")
def index():
    return "render.template"


@app.route("/checkid")
def check():
    _id_ = request.args.get('id')
    if _id_ is not None:
        data = {'server': int(_id_)}
        dt = blacklist.find_one(data)
        return flask.jsonify(
            server=dt["server"],
            reason=dt["reason"],
        )
    else:
        return flask.jsonify({"invalid": "invalid"})


Thread(target=app.run, args=("0.0.0.0", 80)).start()
