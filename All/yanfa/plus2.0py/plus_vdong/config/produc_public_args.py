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
from plus_vdong.common.log import log


configLogMode = 10  # 日志打印级别，值为10: DEBUG_MODE、20: INFO_MODE、30: WARNING_MODE、40: ERROR_MODE
restlogName = 'plus2.0py_log'  # 日志文件路径名/日志器名称
log_path = '/var/log/plus2.0py_log/' # 日志路径
# RESTlogger = MEWDlog.Logger(logMode=configLogMode, logName=restlogName).getLogger()
logger = log.Logger(logMode=configLogMode, logName=restlogName)

# mysqldb 参数
host = 'rm-2ze810q56cy8b4o1a.mysql.rds.aliyuncs.com'
user = 'vd_plus20'
passwd = '9U0Vss2BQ3'
port = '3306'
database = 'vd_plus20_online'

redis_http='127.0.0.1'
redis_port='6379'
redis_password=''

#离线库 参数
off_host = 'rm-2ze810q56cy8b4o1a.mysql.rds.aliyuncs.com'
off_user = 'vd_plus20'
off_passwd = '9U0Vss2BQ3'
off_port = '3306'
off_database = 'vd_plus20_offline'

# elasticsearch addr
es_hosts = ['172.17.0.136:9200','172.17.0.137 :9200']
es_http = '172.17.0.136:9200'

index_dict = {
    'applet': ['page', 'visits', 'event', 'user', 'geo']
}

# etl脚本地址
etl_sh_path = "/data/wwwroot/plus2.0/etl/sh"
