from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from doapi.serializers import *
from doapi.models import *

class Logic():
    def onDataReceived(self,data):
        print "onDataReceived", data
        t, v = DataType.getType(data)
        print "type %s val %s" %( t, v)

        de = DataEntry(d_type=t, value=v)
        de.save()
        self.tryDetectEvent(de)



    def tryDetectEvent(self,de):
        print "try detect event", de.id

