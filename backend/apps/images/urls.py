###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

from django.urls import path, include

from rest_framework import routers

from apps.images.views import OSISOViewSet

router = routers.SimpleRouter()
router.register(u'iso', OSISOViewSet)
#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]

