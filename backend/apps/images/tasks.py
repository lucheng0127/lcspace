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
logging.basicConfig(filename='/opt/log/image_tasks.log', level=logging.INFO, format=format_str)
logger = logging.getLogger()

@job
def upload_iso(file, md5_str, filename):
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
            if iso_md5 == md5_str:
                obj = OSISO.objects.get(md5=md5_str)
                logger.info('get obj id {}'.format(obj.id))
                obj.status = 'FINISHED'
                obj.save()

