#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import time
import urllib2
import urllib
import urlparse

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
            ts = time.mktime(datetime.datetime.strptime(f.split('.')[0], '%Y-%m-%d-%H-%M-%S').timetuple())
            events.append(
                (ts, "/{}/{}".format('static/fuckups', f)))
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

@app.route("/api/achtung")
def achtung():
    keeper.on_event()
    return jsonify(get_state())

@app.route("/api/buy")
def buy():
    ret = urllib2.urlopen(
        'https://api-3t.sandbox.paypal.com/nvp',
        data=urllib.urlencode([
            ("USER", "sdk-three_api1.sdk.com"),
            ("PWD", "QFZCWN5HZM8VBG7Q"),
            ("SIGNATURE", "A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU"),
            ("VERSION", "119"),
            ("PAYMENTREQUEST_0_PAYMENTACTION", "Sale"),
            ("PAYMENTREQUEST_0_CUSTOM", "BEER!!!"),
            ("PAYMENTREQUEST_0_AMT", "500"),
            ("PAYMENTREQUEST_0_CURRENCYCODE", "RUB"),
            ("RETURNURL", "https://localhost:5000"),
            ("CANCELURL", "https://localhost:5000"),
            ("METHOD", "SetExpressCheckout"),
        ])
    ).read()
    return jsonify(urlparse.parse_qs(ret))

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
    return app.send_static_file('./beer-keeper.html')

if __name__ == "__main__":
    reset_storage()
    sl = SensorListener()
    sl.add_callback(keeper.keep, 'light')
    #sl.launch()
    app.debug = True
    app.run()
