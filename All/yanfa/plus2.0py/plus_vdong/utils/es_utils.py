# -*- coding: utf-8 -*-
#*******************************************************************************************
# **  文件名称：es_utils.py
# **  功能描述：调度指标计算
# **
# **  创建者:   小强强 sunshuqiang@vdongchina.com
# **  创建日期: 2018-12-10
# **  修改日志:
# **  修改日期: 修改人   修改应用
# ** ---------------------------------------------------------------------------------------
# **
# ** ---------------------------------------------------------------------------------------
# **
# **  程序调用格式：
# **
#********************************************************************************************
import json
import urllib2

from elasticsearch import Elasticsearch

from plus_vdong.common.static import public_args

es = Elasticsearch(public_args.es_hosts)

def get_request(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    result = response.read()
    result_json = json.loads(result)
    return result_json

def post_request(url,values):
    params = json.dumps(values)
    headers = {"Content-type":"application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    result = response.read()
    result_json = json.loads(result)
    return result_json

def es_bulk(indexname,values):
    res = es.bulk(index=indexname,  doc_type = 'doc', body = values)
    return res

def index_exists(index_name):
    res = es.indices.exists(index_name)
    return res

def get_id(index_name,doc_id):
    res = es.get(index_name,"doc",doc_id)
    return res
