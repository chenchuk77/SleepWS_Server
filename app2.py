#!flask/bin/python
from flask import Flask, jsonify
import time
import json
import sys
from datetime import datetime
import os

current_milli_time = lambda: int(round(time.time() * 1000))
data = {}

app = Flask(__name__)


@app.route('/sleepws/ping', methods=['GET'])
def get_ping():
    return jsonify({'ping': 'pong'})


@app.route('/sleepws/getall', methods=['GET'])
def get_all():
    return jsonify({'data': data})

@app.route('/sleepws/sleep/<timestamp>', methods=['GET'])
def add_sleep_record(timestamp):
    data[timestamp]='sleep'
    return jsonify({'sleep': timestamp})

@app.route('/sleepws/wakeup/<timestamp>', methods=['GET'])
def add_wakeup_record(timestamp):
    data[timestamp]='wakeup'
    return jsonify({'wakeup': timestamp})

if __name__ == '__main__':
    app.run(debug=True)
    #data = {}
