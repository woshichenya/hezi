# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  文件名称：public_args.py
# **  功能描述：公共参数类
# **
# **  创 建 者: 小强强 sunshuqiang@vdongchina.com
# **  创建日期: 2018-12-10
# **  修改日志:
# **  修改日期: 修改人   修改应用
# ** ---------------------------------------------------------------------------------------
# **
# ** ---------------------------------------------------------------------------------------
# **
# **  程序调用格式：
# **
# ********************************************************************************************

# 设置日志参数
from data_stats.common.log import log


configLogMode = 10  # 日志打印级别，值为10: DEBUG_MODE、20: INFO_MODE、30: WARNING_MODE、40: ERROR_MODE
restlogName = 'data_company_stats'  # 日志文件路径名/日志器名称
log_path = '/var/log/data_company_stats/' # 日志路径
# RESTlogger = MEWDlog.Logger(logMode=configLogMode, logName=restlogName).getLogger()
logger = log.Logger(logMode=configLogMode, logName=restlogName)

# mysqldb 参数
host = '39.107.239.18'
user = 'root'
passwd = 'wdtx.2016'
port = '3306'
database = 'data_company_stats'

#离线库 参数
off_host = '39.107.239.18'
off_user = 'root'
off_passwd = 'wdtx.2016'
off_port = '3306'
off_database = 'data_company_stats'


redis_http='127.0.0.1'
redis_port='6379'
redis_password=''


# elasticsearch addr
es_hosts = ['172.17.0.136:9200','172.17.0.137 :9200']
es_http = '172.17.0.136:9200'

index_dict = {
    'applet': ['page', 'visits', 'event', 'user', 'geo']
}

# etl脚本地址
etl_sh_path = "/data/wwwroot/plus2.0/etl/sh"
