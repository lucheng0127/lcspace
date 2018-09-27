###########################
# author: lucheng         #
# create date: 2018/09/13 #
###########################
#_*_ coding: utf-8 _*_

import os
import subprocess
import logging

from django_rq import job

from apps.images.models import OSISO

format_str = '%(levelname)s: %(asctime)s %(message)s'
logging.basicConfig(filename='/opt/log/rq_tasks.log', level=logging.INFO, format=format_str)
logger = logging.getLogger()

@job
def upload_iso(file, obj_id, filename):
    with open(os.path.join('/opt/iso', filename), 'wb+') as dst_f:
        for chunk in file.chunks():
            dst_f.write(chunk)
        dst_f.close()
        logger.info('file {} upload succeed'.format(filename))
        file_path = os.path.join('/opt/iso', filename)
        args = ['md5sum']
        args.append(os.path.join(file_path))
        logger.info(args)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        logger.info(stdout)
        if not stderr:
            iso_md5 = str(stdout)[2:34]
            logger.info('file md5 str is \n{}'.format(iso_md5))
            obj = OSISO.objects.get(id=obj_id)
            logger.info('get obj id {}'.format(obj.id))
            md5_str = obj.md5
            if iso_md5 == md5_str:
                logger.info('iso file {} upload succeed!'.format(filename))
                obj.status = 'FINISHED'
                obj.save()
            else:
                logger.error('iso file {} upload failed, MD5 not match!'.format(filename))
                obj.status = 'FAILED'
                obj.save()
                if os.path.isfile(os.path.join('/opt/iso', filename)):
                    os.remove(os.path.join('/opt/iso', filename))

