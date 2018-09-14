###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

import time

from django.db import models


class OSISO(models.Model):
    OS_CHOICES = (
        ('Linux', 'Linux'),
        ('Windows', 'Microsoft Windows'),
        ('BSD', 'BSD'),
        ('Unix', 'Unix'),
        ('MacOS', 'MacOS'),
        ('Other', 'Other'),
    )

    STATUS_CHOICES = (
        ('FINISHED', u'上传完成'),
        ('UPLOADING', u'上传中'),
        ('WAITING', u'等待上传'),
        ('FAILED', u'上传失败'),
    )

    id = models.AutoField(primary_key=True)
    os_type = models.CharField(max_length=10, choices=OS_CHOICES, default='Linux')
    md5 = models.CharField(max_length=32, null=False, blank=True, default='', unique=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    iso = models.FileField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UPLOADING')

    @property
    def name(self):
        return str(self.iso.name).split('/')[-1]

    @property
    def status_cn(self):
        return self.get_status_display()

    @property
    def upload_time_str(self):
        return self.upload_time.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        db_table = 'os_iso'

