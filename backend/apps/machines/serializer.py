###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

from rest_framework import serializers

from apps.machines.models import VMachines, MachineConfig


class MachineConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineConfig
        fields = '__all__'
        read_only_filelds = ('id', 'device')


class VMachinesSerializer(serializers.ModelSerializer):
    configs = MachineConfigSerializer()

    class Meta:
        model = VMachines
        fields = ('id', 'name', 'uuid', 'create_time_str', 'configs',)
        read_only_filelds = ('id', 'uuid', 'create_time_str')

