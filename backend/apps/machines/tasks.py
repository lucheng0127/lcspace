###########################
# author: lucheng         #
# create date: 2018/09/23 #
###########################
#_*_ coding: utf-8 _*_

from django_rq import job

@job
def create_vm():
    pass

@job
def create_img():
    pass

