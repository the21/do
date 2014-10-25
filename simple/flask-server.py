#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import time

from hack import  SensorListener, play_sound, save_photo
from flask import Flask, jsonify
app = Flask(__name__)

CURDIR = os.path.dirname(os.path.realpath(__file__))


def reset_storage():
    static_dir = os.path.join(CURDIR, 'static', 'fuckups')
    for f in os.listdir(static_dir):
        if f.endswith('.jpg'):
            os.remove(os.path.join(static_dir, f))

class RefrigeratorKeeper(object):
    def __init__(self):
        self.is_open = True
        self.attempt_name = None
        self.last_reset = None

    def turnedon(self):
        return self.attempt_name is not None

    def on_event(self):
        now = datetime.datetime.now()
        fname = os.path.join(CURDIR, 'static/fuckups/{}.jpg'.format(now.strftime('%Y-%m-%d-%H-%M-%S')))
        save_photo(fname)
        play_sound(os.path.join(CURDIR, '..', 'resource', 'alarm.mp3'))
        self.last_reset = datetime.datetime.now()

    def start(self):
        self.attempt_name = 'foo'
        self.last_reset = datetime.datetime.now()

    def stop(self):
        self.last_reset = None
        self.attempt_name = None
        self.is_open = True
        reset_storage()

    def keep(self, light):
        if not self.attempt_name:
            return
        if light < 10:
            self.is_open = False
        elif not self.is_open:
            self.is_open = True
            self.on_event()

keeper = RefrigeratorKeeper()

def get_state():
    events = []
    static_dir = os.path.join(CURDIR, 'static', 'fuckups')
    for f in os.listdir(static_dir):
        if f.endswith('.jpg'):
            events.append(
                (f.split('.')[0],
                 "/{}/{}".format('static/fuckups', f)))
    events.sort()
    if keeper.last_reset:
        last_reset = time.mktime(keeper.last_reset.timetuple())
    else:
        last_reset = 0
    return {
        'isOn': keeper.turnedon(),
        'lastReset': last_reset,
        'events': events
    }

@app.route("/api/events")
def get_events():
    return jsonify(get_state())

@app.route("/api/start")
def start_keeper():
    keeper.start()
    return jsonify(get_state())

@app.route("/api/stop")
def stop_keeper():
    keeper.stop()
    return jsonify(get_state())

@app.route("/")
def index_html():
    return app.send_static_file('./index.html')

if __name__ == "__main__":
    reset_storage()
    sl = SensorListener()
    sl.add_callback(keeper.keep, 'light')
    sl.launch()
    app.debug = True
    app.run()
