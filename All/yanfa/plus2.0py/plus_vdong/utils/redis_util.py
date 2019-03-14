# -*- coding:utf-8 -*-
# ****************************************************************************
# ** 创建时间：2018-12-10
# ** 创建者：tangyonghcun
#
# ** 文件名：redis_util.py
# ** 功能描述：封装redis的api
#
# ****************************************************************************

import redis
from plus_vdong.common.static import public_args as p_a

# 使用连接池连接数据库。这样就可以实现多个Redis实例共享一个连接池
if p_a.redis_password:
    pool = redis.ConnectionPool(host=p_a.redis_http, port=p_a.redis_port,password=p_a.redis_password)
else:
    pool = redis.ConnectionPool(host=p_a.redis_http, port=p_a.redis_port)
redis_db = redis.Redis(connection_pool=pool)
