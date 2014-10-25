from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
# from django.utils import timezone 

class DataType:
    UNKNOWN = 0
    TEMP = 1
    SOUND = 2
    LIGHT = 3

    CHOICES = (
        (UNKNOWN, "UNKNOWN"),
        (TEMP, "TEMP"),
        (SOUND, "SOUND"),
        (LIGHT, "LIGHT")
    )

    @classmethod
    def getType(cls, data):
        if not data:
            return (cls.UNKNOWN,0)
        elif "light" in data:
            return (cls.LIGHT, data["light"])
        elif "temp" in data:
            return (cls.TEMP, data["temp"])
        elif "snd_level" in data:
            return (cls.SOUND, data["snd_level"])

        return (cls.UNKNOWN,0)


class DataEntry(models.Model):
    d_type = models.IntegerField(
        choices=DataType.CHOICES, default=DataType.UNKNOWN)
    value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return "{%s} value=%s time=%s" % (self.d_type, self.value, self.pub_time)

class Listener(models.Model):
    title = models.CharField(default="", max_length=120)
    d_type = models.IntegerField(
        choices=DataType.CHOICES, default=DataType.UNKNOWN)
    save_all_checks = models.BooleanField(default=False)
    min_value = models.IntegerField(default=0)
    max_value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    min_time_value = models.TimeField(blank=True, null=True)
    max_time_value = models.TimeField(blank=True, null=True)
    creator = models.ForeignKey(User, related_name="listeners")

    def __unicode__(self):
        return "{%s} %s value=[%s;%s] time=[%s,%s]" % (self.d_type, self.title, self.min_value, self.max_value, self.min_time_value, self.max_time_value)


class Event(models.Model):
    listener = models.ForeignKey(Listener, related_name="events")
    data = models.ForeignKey(DataEntry, related_name="events")
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s | %s" % (self.data, self.listener)

