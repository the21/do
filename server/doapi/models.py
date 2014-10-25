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

    def __unicode__(self):
        return "%s (%s)" % (self.value, self.d_type)

class Listener(models.Model):
    title = models.CharField(max_length=120)
    save_all_checks = models.BooleanField(default=False)
    min_value = models.IntegerField(default=0)
    max_value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    min_time_value = models.DateTimeField(blank=True, null=True)
    max_time_value = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(User, related_name="listeners")


    def __unicode__(self):
        return "%s (%s)" % (self.title, self.id)


class Event(models.Model):
    listener = models.ForeignKey(User, related_name="events")
    data = models.ForeignKey(DataEntry, related_name="events")
    pub_date = models.DateTimeField(auto_now_add=True)

