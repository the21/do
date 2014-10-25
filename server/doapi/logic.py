from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from doapi.serializers import *
from doapi.models import *
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

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
            if (l.min_value == 0 and l.max_value == 0) or (l.min_value <= data.value <= l.max_value):
                if (not l.min_time_value and not l.max_time_value) or l.min_time_value <= data.pub_time <= l.max_time_value:
                    return True
        return False

    def onEvent(self,event):
        print "!event processing %s" % event
        text = get_template('notification_email.txt')
        html = get_template('notification_email.html')
        
        context = Context({
            'event': event
            })

        subject = event.listener.title

        text_content = text.render(context)
        html_content = html.render(context)
        bcc = []
        to = event.listener.creator.email
        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, to=[to], cc=bcc)
        msg.attach_alternative(html_content, "text/html")
        msg.send()





