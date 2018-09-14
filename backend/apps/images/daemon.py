###########################
# author: lucheng         #
# create date: 2018/09/12 #
# daemon scan iso direct  #
###########################
#_*_ coding: utf-8 _*_

import os
import sys
import time
import hashlib
import subprocess
import django


# set django env
sys.path.insert(0, '/opt/workspace/lcspace/backend')
os.environ['DJANGO_SETTINGS_MODULE'] = 'index.settings'
django.setup()

from apps.images.models import OSISO

def main():
    obj_mds_list = [i.md5 for i in OSISO.objects.all()]
    isos = [i for i in os.listdir('/opt/iso') if os.path.isfile(os.path.join('/opt/iso', i)) and os.path.splitext(i)[1] == '.iso']
    for iso in isos:
        file = os.path.join('/opt/iso', iso)
        args = ['md5sum']
        args.append(file)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if not stderr:
            iso_md5 = str(stdout)[2:34]
        else:
            print('get md5 failed for {}'.format(file))
            continue
        if iso_md5 not in obj_mds_list:
            obj_cache = OSISO(md5=iso_md5, iso=file, status='FINISHED')
            obj_cache.save()
            continue
        else:
            obj = OSISO.objects.get(md5=iso_md5)
            obj.status = 'FINISHED'
            obj.save()
            continue

if __name__ == '__main__':
    main()
