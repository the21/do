#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

from hack import  SensorListener, play_sound
from flask import Flask, jsonify
app = Flask(__name__)

CURDIR = os.path.dirname(os.path.realpath(__file__))

def new_event():
    now = datetime.datetime.now()

class RefrigeratorKeeper(object):
    def __init__(self):
        self.is_open = True
        self.attempt_name = None

    def start(self):
        self.attempt_name = 'foo'

    def stop(self):
        self.attempt_name = None
        self.is_open = True

    def keep(self, light):
        if not self.attempt_name:
            print '.'
            return
        print light
        if light < 10:
            self.is_open = False
        elif not self.is_open:
            self.is_open = True
            print "ACHTUNG!!!!"
            play_sound(os.path.join(CURDIR, '..', 'resource', 'alarm.mp3'))
            #save_photo('/home/ermolovd/face.jpg')

keeper = RefrigeratorKeeper()

@app.route("/api/start")
def start_keeper():
    keeper.start()
    return jsonify({'status': 'ok'})

@app.route("/api/stop")
def stop_keeper():
    keeper.stop()
    return jsonify({'status': 'ok'})

@app.route("/")
def index_html():
    return app.send_static_file('./index.html')

if __name__ == "__main__":
    sl = SensorListener()
    sl.add_callback(keeper.keep, 'light')
    sl.launch()
    app.debug = True
    app.run()
