from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from doapi.serializers import *
from doapi.models import *

class Logic():
    def onDataReceived(self,data):
        t, v = DataType.getType(data)
        # print "type %s val %s" %( t, v)

        de = DataEntry(d_type=t, value=v)
        de.save()
        self.tryDetectEvent(de)



    def tryDetectEvent(self,data):
        print "try detect event '%s'"%( data)
        ls = Listener.objects.filter(d_type=data.d_type)
        createdEvents = []
        for l in ls:
            if self.isEvent(l,data):
                # print "event found", l.title, data
                e = Event(listener=l,data=data)
                e.save()
                createdEvents.append(e)

        for e in createdEvents:
            self.onEvent(e)


    def isEvent(self, l, data):
        if l.save_all_checks:
            return True

        if data.d_type == l.d_type:
            if (l.min_value == 0 and l.min_value == 0) or l.min_value <= data.value <= l.max_value:
                if (not l.min_time_value and not l.max_time_value) or l.min_time_value <= data.pub_time <= l.max_time_value:
                    return True
        return False

    def onEvent(self,event):
        print "event processing %s" % event





