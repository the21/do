from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from doapi import views
from doapi import logic
import random
# from doapi import hack

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'entries', views.DataEntryViewSet)
router.register(r'listeners', views.ListenerViewSet)
router.register(r'events', views.EventViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^v0/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)


l = logic.Logic()
debug = True

if not debug:
    a = 2
    # sl = hack.SensorListener()
    # sl.add_callback(l.onDataReceived, None)
    # sl.launch()
else:
    types = ["light","temp","snd_level"]
    def getRandomData():
        return { types[random.randint(0,len(types)-1)]: random.randint(0,100) }

    for x in range(0, 5):
        # print "data %s" % ( getRandomData() )
        l.onDataReceived(getRandomData())


