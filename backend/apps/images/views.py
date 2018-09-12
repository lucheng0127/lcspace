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
    queryset = OSISO.objects.all()
    serializer_class = OSISOSerializer
    permission_classes = []

    def list(self, request):
       isos = [i for i in os.listdir('/opt/iso') if os.path.isfile(os.path.join('/opt/iso', i)) and os.path.splitext(i)[1] == '.iso']
       return Response({'data': isos}, status=status.HTTP_200_OK)
    
    def create(self, request):
        pass

    def destroy(self, request, pk=None):
        pass
       

# hashlib.md5(str(open('models.py').read()).encode('utf-8')).hexdigest()
