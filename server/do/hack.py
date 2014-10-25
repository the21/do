#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import Pubnub
from urllib2 import Request, urlopen, URLError

logging.basicConfig(level=logging.INFO)


try:
    import pygame
    import pygame.camera
    import pygame.image
    USE_PYGAME = True
except ImportError:
    USE_PYGAME = False

if USE_PYGAME:
    pygame.init()
    pygame.mixer.init()
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])

    def save_photo(path):
        print 'saving'
        try:
            cam.start()
            img = cam.get_image()
            pygame.image.save(img, path)
            cam.stop()
        except:
            pass

    def play_sound(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

else:
    def save_photo(path):
        pass

    def play_sound(path):
        pass

app_id = '6d639b4d-7e4d-4c34-a7d2-f410d119d193'
client_id = '0K9ctCl_VWVjj04OFSlOCDLNH.X1FouS'
secret_id = '4_EL2H.lsyznY0jOIcaYWOk7Dp4A4ag.'
token = 'L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC'
light_id = 'ba370b21-2205-4e32-890f-842e8604cbd2'

sound_id = '077cbc8c-eece-4b6e-9bd6-fcb74ce13a27'

token = 'tK1fdG7oU7Af94hN-70bxw0kKPxg4n4F'

def get_connection_info(device):
    device_id = {
        'light': 'ba370b21-2205-4e32-890f-842e8604cbd2',
        'sound': '077cbc8c-eece-4b6e-9bd6-fcb74ce13a27',
        'temperature': '199209ec-ff32-472c-b904-cc0d527a30ab',
    }
    url = 'https://api.relayr.io/apps/{}/devices/{}'.format(app_id, device_id[device])
    request = Request(url)
    request.add_header("Authorization", "Bearer {}".format(token))

    response_body = urlopen(request, "").read()
    #   response = "{
    #       u'authKey': u'e429e82f-bcbb-4dfd-befb-2480cad49e99',
    #       u'subscribeKey': u'sub-c-a84c8b9a-1314-11e4-8bd3-02ee2ddab7fe',
    #       u'cipherKey': u'82e21e2cc9705b38a8006a68b1067491cd2471c4d290dd5fa21247fab090586e',
    #       u'channel': u'84f15d76-0e80-45a9-8514-835fba2dc4f7:9221beff-2e4f-4a1c-86b2-5544f31ad554'
    #       }"
    return json.loads(response_body)

def connect_to_device(device, on_ok, on_error):
    conninfo = get_connection_info(device)
    pubnub = Pubnub.Pubnub(
        publish_key=conninfo['subscribeKey'],
        subscribe_key=conninfo['subscribeKey'],
        cipher_key=conninfo['cipherKey'],
        auth_key=conninfo['authKey']
    )
    channel = conninfo['channel']
    pubnub.subscribe(channel, callback=on_ok, error=on_error)
    return pubnub


class SensorListener(object):
    def __init__(self):
        self.callback_list = []

    def add_callback(self, callback, key_of_interest):
        self.callback_list.append((callback, key_of_interest))

    def on_ok(self, message, channel):
        logging.info('got some data: {}'.format(message))
        data = json.loads(message)
        for cb, key_of_interest in self.callback_list:
            if key_of_interest:
                if key_of_interest in data:
                    cb(data[key_of_interest])
            else:
                cb(data)

    def on_error(self, message):
        logging.error('pubnub error: {}'.format(message))

    def launch(self):
        connect_to_device('light', self.on_ok, self.on_error)
        connect_to_device('sound', self.on_ok, self.on_error)
        connect_to_device('temperature', self.on_ok, self.on_error)
        print 'everything started'

class RefrigeratorKeeper(object):
    def __init__(self):
        self.is_open = True

    def keep(self, data):
        light = data['light']
        print light, data
        if light < 10:
            self.is_open = False
        elif not self.is_open:
            self.is_open = True
            save_photo('/home/ermolovd/face.jpg')

class BeerKeeper(object):
    def __init__(self):
        self.missing = False
        self.init_prox = None

    def keep(self, prox):
        if self.init_prox is None:
            self.init_prox = prox
        elif prox < self.init_prox / 2:
            play_sound('/home/ermolovd/alarm.mp3')
            print 'BEER IS MISSING!!!!!!'


if __name__ == '__main__':
    sl = SensorListener()
    #sl.add_callback(RefrigeratorKeeper().keep, 'light')
    sl.add_callback(BeerKeeper().keep, 'prox')
    sl.launch()
