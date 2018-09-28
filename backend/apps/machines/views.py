###########################
# author: lucheng         #
# create date: 2018/09/23 #
###########################
#_*_ coding: utf-8 _*_

from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.machines.models import VMachines, MachineConfig
from apps.machines.serializer import VMachinesSerializer
from apps.machines.tasks import create_vm_task


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
        name = request.data.get('name')
        configs = request.data.get('configs')
        size = request.data.get('configs.disk_size')
        iso = request.data.get('configs.iso')
        mem = request.data.get('configs.memory')
        vcpu = request.data.get('configs.vcpu')
        device = VMachines(name=name)
        device.save()
        device_conf = MachineConfig(memory=mem, vcpu=vcpu, disk_size=size, iso=iso, img=str(name) + '.img', device=device)
        device_conf.save()
        dom = create_vm_task.delay(None, name, mem, vcpu, size, iso)

        return Response(status=status.HTTP_200_OK)

