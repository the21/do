from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from doapi.serializers import *
from doapi.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DataEntryViewSet(viewsets.ModelViewSet):
    """
    Data received from hardware
    """
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

class ListenerViewSet(viewsets.ModelViewSet):
    """
    Listeners to check data for different conditions
    """
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    Events which was triggered by any listeners
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer