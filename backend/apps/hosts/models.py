###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

from django.db import models


class Hosts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=False, blank=False)
    conn_type = models.CharField(max_length=10, default='default')
    user = models.CharField(max_length=32, default='root')
    password = models.CharField(max_length=32, null=True, blank=True)
    key_file = models.FileField()

    class Meta:
      db_table = 'hosts'

