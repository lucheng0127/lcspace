###########################
# author: lucheng         #
# create date: 2018/09/23 #
###########################
#_*_ coding: utf-8 _*_

from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.machines.models import VMachines, MachineConfig
from apps.machines.serializer import VMachinesSerializer


class MachineViewSet(viewsets.ModelViewSet):
    """
    virtual machine life cycle

    list:
    list all guest machines on host

    create:
    define a new guest machine

    destroy:
    remove a guest machine
    """
    queryset = VMachines.objects.all()
    serializer_class = VMachinesSerializer

    def create(self, request):
        print(request.data)
        return Response(status=status.HTTP_200_OK)

