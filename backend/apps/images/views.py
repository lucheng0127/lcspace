###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

import hashlib
import os

import django_rq

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from apps.images.models import OSISO
from apps.images.serializers import OSISOSerializer
from apps.images.tasks import upload_iso

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
        os_type = request.data.get('os_type')
        md5 = request.data.get('md5')
        iso_f = request.FILES['iso']

        # 特殊字符校验

        # 保存数据，并上传文件
        try:
            obj = OSISO(os_type=os_type, md5=md5, iso=os.path.join('/opt/iso', iso_f.name))
            obj.save()
            upload_iso.delay(iso_f, md5)
            return Response({'data': OSISOSerializer(obj).data, 'msg': 'Created!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg': 'Upload failed!'}, status=status.HTTP_400_BAD_REQUEST)
            

    def destroy(self, request, pk=None):
        pass
       

# hashlib.md5(str(open('models.py').read()).encode('utf-8')).hexdigest()
