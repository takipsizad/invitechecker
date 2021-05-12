import flask
from flask import request
from flask import Flask
from threading import Thread
import pymongo

app=Flask("")


@app.route("/")
def index():
    return "render.template"

@app.route("/checkid")
def check():
    _id = request.args.get('id')
    if _id is not None:
        return "{}".format(_id)
    else:
        return flask.jsonify({"invalid":"invalid"})


Thread(target=app.run,args=("0.0.0.0",80)).start()
