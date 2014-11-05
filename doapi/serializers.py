from django.contrib.auth.models import User, Group
from rest_framework import serializers
from doapi.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DataEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataEntry
        # fields = ('url', 'username', 'email', 'groups')

class ListenerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listener
        # fields = ('url', 'name')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        # fields = ('url', 'name')