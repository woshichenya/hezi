# -*- coding: utf-8 -*-
import os
import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
from data_stats.utils import date_utils
from data_stats.common.static import  public_args as p_a

# from data_stats.common.static import public_args as p_a

if __name__ == "__main__":
    try:
        from elasticsearch import Elasticsearch
    except Exception:
        os.system('pip install elasticsearch')

    try:
        import redis
    except Exception:
        os.system('pip install redis')
    try:
        from peewee import *
    except Exception:
        os.system('pip install peewee')
        os.system('pip install MySQL-python')
        os.system('yum -y install MySQL-python')
    # log_path = p_a.log_path
    log_path = '/var/log/plus2.0py_log/'
    if os.path.exists(log_path) is False:
        os.makedirs(log_path)
    source_path = r'/usr/local/sbin/plus2.0py/data_stats/config'
    goal_path = r'/usr/local/sbin/plus2.0py/data_stats/common/static'
    # branch
    try:
        branch = sys.argv[1].replace(" ", "")
    except Exception:
        branch = ""
    # tag
    try:
        tag = sys.argv[2].replace(" ", "")
    except Exception:
        tag = ""
    try:
        env_name = 'dev'
        if cmp(tag, "") != 0:
            env_name = 'produc'
        elif cmp(branch, "") != 0:
            # p_a.logger.getLogger().debug(branch)
            # branchs = branch.split("/")
            # branch = branchs[1]
            if cmp('master',branch) == 0:
                env_name = 'test'
        os.system('/usr/bin/mv -fb %s/%s_public_args.py %s/public_args.py' %(source_path,env_name,goal_path))
    except Exception, e:
        print 'error ----'

        os.system('/usr/bin/mv -fb %s/%s_public_args.py %s/public_args.py' %(source_path,'dev',goal_path))

    # os.chdir('/usr/local/sbin/plus_spider')
    cron = r'/var/spool/cron/'
    if not os.path.exists(cron):
        os.makedirs(cron)
    cron_file = cron + 'root'
    if os.path.exists(cron_file):
        os.system('/usr/bin/cp %s %s%s' %(cron_file, cron_file, '.'+ date_utils.system_time().replace(' ','').replace(':','')))
    os.system('sed -i -e "/\/data\/wwwroot\/plus2.0\/etl\/sh\/kettle*/d" /var/spool/cron/root')
    os.system('sed -i -e "/\/usr\/local\/sbin\/plus2.0py*/d" /var/spool/cron/root')
    os.system('sed -i -e "/\/usr\/local\/php7\/bin\/php \/data\/wwwroot\/plus2.0*/d" /var/spool/cron/root')

    # os.system('echo "0 0 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/truncate_tables.py > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "0 0 * * * source /data/wwwroot/plus2.0/etl/sh/kettle.py > /dev/null 2>&1" >> %s '% cron_file)
    # os.system('echo "0 */1 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/shop_hour.py > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "1 8 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/key_secret.py > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "1 0 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/uniacids.py > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "*/15 * * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/uniacid_15_min.py > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "*/31 * * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php request_uri="/data/index/index" 1133,1016 > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "1 0 * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php request_uri="/data/index/wechats" 1133,1016 > /dev/null 2>&1" >> %s ' % cron_file)
    # os.system('echo "1 0 * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php request_uri="/data/index/wxapp" 1133,1016 > /dev/null 2>&1" >> %s ' % cron_file)
    #正式版演示数据
    os.system('echo "0 0 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/truncate_tables.py > /dev/null 2>&1" >> %s ' % cron_file)
    os.system('echo "0 */3 * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php  request_uri="/data/demodata/Realtime" 1096 > /dev/null 2>&1" >> %s ' % cron_file)
    os.system('echo "0 2 * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php  request_uri="/data/index/Multdatewxtong" 1096 > /dev/null 2>&1" >> %s ' % cron_file)
    os.system('echo "0 2 * * * /usr/local/php7/bin/php /data/wwwroot/plus2.0/index.php  request_uri="/data/demodata/index" 1096 > /dev/null 2>&1" >> %s ' % cron_file)
    os.system('echo "0 3 * * * /usr/bin/python /usr/local/sbin/plus2.0py/task/compute/user_group.py > /dev/null 2>&1" >> %s ' % cron_file)
