#!flask/bin/python
from flask import Flask, jsonify
import time
import json
import sys
from datetime import datetime
import os

epoch = lambda: int(round(time.time() * 1000))
data = {}
# initialize counter
# counter = 0 if len(data) == 0 else len(data)


app = Flask(__name__)


@app.route('/sleepws/ping', methods=['GET'])
def get_ping():
    return jsonify({'ping': 'pong'})


@app.route('/sleepws/getall', methods=['GET'])
def get_all():
    return jsonify({'data': data})

@app.route('/sleepws/addrecord/<json>', methods=['GET'])
def add_record(json):
    msec = epoch()
    data[msec] = json
    return jsonify({msec: json})

@app.route('/sleepws/wakeup/<json>', methods=['GET'])
def add_wakeup_record(timestamp):
    data[timestamp]='wakeup'
    return jsonify({'wakeup': timestamp})

if __name__ == '__main__':
    app.run(debug=True)
    #data = {}
