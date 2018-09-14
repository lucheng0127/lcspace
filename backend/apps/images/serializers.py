###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

from apps.images.models import OSISO

from rest_framework import serializers


class OSISOSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSISO
        fields = ('id', 'os_type', 'name', 'md5', 'iso', 'status_cn', 'upload_time_str',)
        read_only_fields = ('id', 'name', 'status_cn', 'upload_time_str',)
        extra_kwargs = {
            'iso': {'write_only': True},
        }

