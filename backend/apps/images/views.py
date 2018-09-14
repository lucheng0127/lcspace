###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

import hashlib
import os

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from apps.images.models import OSISO
from apps.images.serializers import OSISOSerializer

class OSISOViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    operate system iso upload, get iso list and delete iso
    """
    queryset = OSISO.objects.all().exclude(status='FAILED')
    serializer_class = OSISOSerializer
    permission_classes = []

    def create(self, request):
        pass

    def destroy(self, request, pk=None):
        pass
       

# hashlib.md5(str(open('models.py').read()).encode('utf-8')).hexdigest()
