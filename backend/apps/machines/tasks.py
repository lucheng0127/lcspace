###########################
# author: lucheng         #
# create date: 2018/09/23 #
###########################
#_*_ coding: utf-8 _*_

import os
import logging

from django_rq import job

from apps.machines.models import VMachines, MachineConfig

from utils.host import Host 
from utils.dom_utils import create_img, ConfigureVM, VMInstance

logger = logging.getLogger()

@job
def create_vm_task(conn, name, mem, cpu_num, disk_size, iso):
    logger.info('Start create new vm\nname %s, mem %s, cpu_num %s, disk_size %s, iso %s', name, mem, cpu_num, disk_size, iso)
    # 判断qemu server是否连接
    if not conn:
        host = Host()
        result = host.connect()
        if int(result['rsp_code']) == 0 and result['data']:
            conn = result['data']
            logger.info('Connected to default QEMU server!')
        else:
            logger.error('No QEMU server connected!')
            return False
    # 根据配置的磁盘大小生成对应的虚拟机镜像
    img_file = str(os.path.join('/opt/vm_img', name)) + '.img'
    disk_size = str(disk_size) + 'G'
    result = create_img(name=img_file, img_size=disk_size)
    if not (int(result['rsp_code']) == 0 and result['data']):
        logger.error('Create vm img field!')
        return False
    logger.info('Create vm img succeed %s', result['data'])
    # 根据配置生成虚拟机xml配置文件
    conf_ins = ConfigureVM()
    iso_file = str(os.path.join('/opt/iso', iso))
    # Mem 用M计算
    mem = str(int(mem) * 1024)
    result = conf_ins.conf_vm(name, mem, cpu_num, img_file, iso_file)
    if not (int(result['rsp_code']) == 0 and result['data']):
        logger.error('Configure vm failed!')
        return False
    xml_file = result['data']
    logger.info('Configure vm succeed, xml file %s', xml_file)
    # 根据xml配置文件创建虚拟机
    device_obj = VMachines.objects.get(name=name)
    vm_ins = VMInstance()
    result = vm_ins.create_vm(conn, xml_file)
    if not (int(result['rsp_code']) == 0 and result['data']):
        logger.error('Create vm failed!')
        device_obj.status = 'Failed'
        device_obj.save()
        # 删除配置文件和镜像
        if os.path.isfile(img_file):
            os.remove(img_file)
        return False
    device_obj.status = 'Running'
    device_obj.uuid = result['data'].UUIDString()
    device_obj.save()
    logger.info('Create vm %s succeed!', name)
    return True

