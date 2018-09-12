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
        fields = '__all__'
        read_only_fields = ('id',)

