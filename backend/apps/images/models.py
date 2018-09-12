###########################
# author: lucheng         #
# create date: 2018/09/12 #
###########################
#_*_ coding: utf-8 _*_

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

    id = models.AutoField(primary_key=True)
    os_type = models.CharField(max_length=10, choices=OS_CHOICES, default='Linux')
    md5 = models.CharField(max_length=32, null=False, blank=True, default='')
    upload_time = models.DateTimeField(auto_now_add=True)
    iso = models.FileField()

    @property
    def name(self):
        return str(self.iso.name).split('/')[-1]

    class Meta:
        db_table = 'os_iso'

