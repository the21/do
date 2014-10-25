#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from urllib2 import Request, urlopen, URLError

#ex = "{
    #u'authKey': u'e429e82f-bcbb-4dfd-befb-2480cad49e99',
    #u'subscribeKey': u'sub-c-a84c8b9a-1314-11e4-8bd3-02ee2ddab7fe',
    #u'cipherKey': u'82e21e2cc9705b38a8006a68b1067491cd2471c4d290dd5fa21247fab090586e',
    #u'channel': u'84f15d76-0e80-45a9-8514-835fba2dc4f7:9221beff-2e4f-4a1c-86b2-5544f31ad554'
    #}"

app_id = '6d639b4d-7e4d-4c34-a7d2-f410d119d193'
client_id = '0K9ctCl_VWVjj04OFSlOCDLNH.X1FouS'
secret_id = '4_EL2H.lsyznY0jOIcaYWOk7Dp4A4ag.'
token = 'L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC'
light_id = 'ba370b21-2205-4e32-890f-842e8604cbd2'

token = 'tK1fdG7oU7Af94hN-70bxw0kKPxg4n4F'

import json
from urllib2 import Request, urlopen
import Pubnub

url = 'https://api.relayr.io/apps/{}/devices/{}'.format(app_id, light_id)
request = Request(url)
request.add_header("Authorization", "Bearer {}".format(token))

response_body = urlopen(request, "").read()
response = json.loads(response_body)

print response

pubnub = Pubnub.Pubnub(
    publish_key=response['subscribeKey'],
    subscribe_key=response['subscribeKey'],
    cipher_key=response['cipherKey'],
    auth_key=response['authKey']
)
channel = response['channel']

def on_ok(message, channel):
    print "got it: ", message, channel

def on_error(message):
    print "wtf?: ", message

pubnub.subscribe(channel, callback=on_ok, error=on_error)
