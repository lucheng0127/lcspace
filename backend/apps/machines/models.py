###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

from django.db import models


class VMachines(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=32, null=True, blank=True)
    name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    @property
    def create_time_str(self):
        return self.create_time.strftime("%Y-%m-%d %H:%M:%S")


    class Meta:
        db_table = 'vmachines'


class MachineConfig(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey('VMachines',
                               on_delete=models.CASCADE,
                               related_name='configs')
    memory = models.IntegerField()
    vcpu = models.IntegerField()
    disk_size = models.IntegerField()
    img = models.CharField(max_length=128, null=True, blank=True)
    iso = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'machine_config'

