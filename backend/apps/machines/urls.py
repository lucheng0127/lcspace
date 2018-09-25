###########################
# author: lucheng         #
# create date: 2018/09/23 #
###########################
#_*_ coding: utf-8 _*_

from django.urls import path, include

from rest_framework import routers

from apps.machines.views import MachineViewSet

router = routers.SimpleRouter()
router.register(u'devices', MachineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

