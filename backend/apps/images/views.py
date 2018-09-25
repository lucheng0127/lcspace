###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

import hashlib
import os
import uuid

import django_rq

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

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
    queryset = OSISO.objects.all()
    serializer_class = OSISOSerializer
    permission_classes = []

    def create(self, request):
        os_type = request.data.get('os_type')
        md5 = request.data.get('md5')
        iso_f = request.FILES['iso']

        # 特殊字符校验
        if not md5 or not iso_f:
            return Response({'msg': u'请选择系统镜像文件,并填写MD5!'}, status=status.HTTP_400_BAD_REQUEST)
        if OSISO.objects.filter(md5=md5):
            return Response({'msg': u'系统镜像已存在!'}, status=status.HTTP_400_BAD_REQUEST)
        # 文件重命名
        f_name, f_type = str(iso_f.name).rsplit('.', 1)
        if str(f_type) != 'iso':
            return Response({'msg': u'请选择正确的系统镜像文件!'}, status=status.HTTP_400_BAD_REQUEST)
        f_name = str(f_name).replace(' ', '') 
        f_name = str(f_name).replace('.', '') 
        f_name = str(f_name).replace('-', '_') 
        f_name = str(f_name).replace('/', '') 
        f_name = f_name + str(uuid.uuid1())[:8] + '.'  + f_type

        # 保存数据，并上传文件
        try:
            obj = OSISO(os_type=os_type, md5=md5, iso=os.path.join('/opt/iso', f_name))
            obj.save()
            upload_iso.delay(iso_f, obj.id, f_name)
            return Response({'data': OSISOSerializer(obj).data, 'msg': 'Created!'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'msg': 'Upload failed!'}, status=status.HTTP_400_BAD_REQUEST)
            

    def destroy(self, request, pk=None):
        obj = get_object_or_404(OSISO, id=pk)
        filename = os.path.join('/opt/iso', obj.name)
        if os.path.isfile(filename):
            os.remove(filename)
        obj.delete()
        return Response({'msg': u'删除系统镜像{}成功!'.format(obj.name)}, status=status.HTTP_200_OK)
        pass
       

    @action(detail=False)
    def os_type(self, request):
        data = dict()
        data['Linux'] = 'Linux'
        data['Windows'] = 'Microsoft Windows'
        data['BSD'] = 'BSD'
        data['Unix'] = 'Unix'
        data['MacOS'] = 'MacOS'
        data['Other'] = 'Other'
        return Response(data, status=status.HTTP_200_OK)

# hashlib.md5(str(open('models.py').read()).encode('utf-8')).hexdigest()
