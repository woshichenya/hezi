# -*- coding: utf-8 -*-
from plus_vdong.all_table_compute.data_source.es_source import local_geocoder as l_g
from plus_vdong.utils import date_utils
from plus_vdong.utils import es_utils
from plus_vdong.common.static import public_args as p_a


def refresh(app_key, name, day):
    """
    刷新索引
    :return 0 为成功
    """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = "http://%s/%s/_refresh" % (p_a.es_http, index)
        req_json = es_utils.get_request(url)
        return req_json["_shards"]["failed"]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s error: %s' % (index, str(e)))
        return 1

def es_post(app_key, name, day, value=None):
    """ es post 请求 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return None
        url = "http://%s/%s/doc/_search?size=0" % (p_a.es_http, index)
        if value is None:
            value = {"query":{"match_all":{}}}
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s error: %s' % (index, str(e)))
        return None

def count(app_key, name, day):
    """  次数 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = "http://%s/%s/doc/_count" % (p_a.es_http, index)
        req_json = es_utils.get_request(url)
        return req_json["count"]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s error: %s' % (index, str(e)))
        return 0

def condition_count(app_key, name, day, query=None):
    """ 条件统计次数 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = "http://%s/%s/doc/_search?size=0" % (p_a.es_http, index)
        value = {"query":{"match_all":{}}}
        if query is not None:
            if query.has_key('query'):
                value = query
            else:
                value['query'] = query
        req_json = es_utils.post_request(url, value)
        return req_json["hits"]["total"]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s error: %s' % (index, str(e)))
        return 0

def uniqueness_count(app_key, name, day, fields, query=None):
    """ 去重次数（唯一次数） """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = "http://%s/%s/doc/_search?size=0" % (p_a.es_http, index)
        field = "%s.keyword" % fields
        value = {"aggs": {"NAME": {"cardinality": {"field": field}}}}
        if query is not None:
            value["query"] = query
        req_json = es_utils.post_request(url, value)
        return req_json["aggregations"]["NAME"]["value"]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return 0


def grades_stats(app_key, name, day, fields, aggs_type, query=None):
    """ 计算sun、min、avg、max、count """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = "http://%s/%s/doc/_search?size=0" % (p_a.es_http, index)
        # if cmp(date_utils.system_time_befor(), day) == 0:
        #     index = "logstash-%s-%s-today-%s" % (app_key, name, day)
        value = {"aggs": {"grades_stats": {"extended_stats": {"field": fields}}}}
        if query is not None:
            value["query"] = query
        req_json = es_utils.post_request(url, value)
        if req_json["aggregations"]["grades_stats"][aggs_type] is None:
            return 0
        else:
            return req_json["aggregations"]["grades_stats"][aggs_type]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return 0


def terms_aggs(app_key, name, day, fields, query=None, child_aggs=None):
    """ 按 terms 聚合 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return None
        url = "http://%s/%s/doc/_search?size=0" % (p_a.es_http, index)
        field = "%s.keyword" % fields
        value = {"aggs": {"NAME": {"terms": {"field": field, "size": 2000000000, "order": {"_count": "asc"}}}}}
        if query is not None:
            value["query"] = query
        if child_aggs is not None:
            value["aggs"]["NAME"]["aggs"] = child_aggs
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return None


def add_alias(app_key, name, day):
    """
    添加索引别名
    添加成功放回 true
    """
    index = ''
    try:
        url = "http://%s/_aliases" % p_a.es_http
        index = "logstash-%s-%s-%s" % (app_key, name, date_utils.param_day_yesterday(day))
        if es_utils.index_exists(index) is False:
            return True
        index_alias = "logstash-%s-%s" % (app_key, name)
        value = {"actions": [{"add": {"index": index, "alias": index_alias}}]}
        req_json = es_utils.post_request(url, value)
        return req_json["acknowledged"]
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return False


def page_query(app_key, name, day, _from=0, size=20, order="desc", query=None):
    """ 分页查询 """
    if query is None:
        query = {"match_all": {}}
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return None
        url = "http://%s/%s/doc/_search" % (p_a.es_http, index)
        value = {"query": query, "from": _from, "size": size, "sort": [{"@timestamp": {"order": order}}]}
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return None


def query_id(app_key, name, doc_id, day):
    """ 根据id查询 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return None
        url = "http://%s/%s/doc/%s" % (p_a.es_http, index, doc_id)
        req_json = es_utils.get_request(url)
        # req_json = es_utils.get_id(index, doc_id)
        if req_json["found"] is False:
            return None
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s error: %s' % (url, str(e)))
        return None


def date_aggs_hour(app_key, name, day, time, query=None, aggs=None):
    """按小时聚合时间段内的数据"""
    index = ''
    try:
        index = 'logstash-%s-%s-%s' % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = 'http://%s/%s/doc/_search?size=0' % (p_a.es_http, index)
        value = {"aggs": {"sales_over_time": {
            "date_histogram": {"field": "@timestamp", "interval": time, "format": "yyyy-MM-dd HH:mm"}}}}
        if query is not None:
            value['query'] = query
        if aggs is not None:
            value['aggs']['sales_over_time']['aggs'] = aggs
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return 0


def query_ids(app_key, name, day, _ids):
    """ 根据多个id查询 """
    index = ''
    try:
        index = "logstash-%s-%s-%s" % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return None
        url = "http://%s/%s/doc/_search" % (p_a.es_http, index)
        value = {"query": {"terms": {"_id": _ids}}, "sort": [{"day": {"order": "desc"}}]}
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('index: %s jsonbody: %s error: %s' % (index, value, str(e)))
        return None


def query_user_game_stay_hour(app_key,name,day,time,order,query=None):
    index = ''
    try:
        index = 'logstash-%s-%s-%s' % (app_key, name, day)
        if es_utils.index_exists(index) is False:
            return 0
        url = 'http://%s/%s/doc/_search?size=0' % (p_a.es_http, index)
        value = {"aggs": {"sales_over_time": {
            "date_histogram": {"field": "@timestamp", "interval": time, "format": "yyyy-MM-dd HH:mm"}}},
            'query': {"range": {"@timestamp": {"gte": date_utils.now_time_start(), "lt": date_utils.now_time_end()}}},
            'aggs': {"NAME": {"terms": {"field": "uuid_userMarker.keyword", "size": 6000000},
                              "aggs": {"NAME": {"top_hits": {"size": 1, "sort": [{"@timestamp": {"order": order}}]}}}}}}
        req_json = es_utils.post_request(url, value)
        return req_json
    except Exception, e:
        p_a.logger.getLogger().error('%s terms_aggs %s' % (index, str(e)))
        return 0


# 查询经纬度(分页)
def query_lat_lng(app_key,name,day):
    res_index = []
    local_index = []
    try:
        # 计算总条数
        num = count(app_key,name,day)
        # 计算偏移次数(不足一次往前补)
        for_num = int((num+20-1)/20)
        offset = 0
        for _ in range(for_num):
            index = "logstash-%s-%s-%s" % (app_key, name, day)
            url = "http://%s/%s/doc/_search" % (p_a.es_http, index)
            value = {"from":offset,"size":20,"query":{"bool":{"must_not":[{"exists":{"field":"lat.keyword"}}]}},"_source":["lat","lng","uuid"]}
            result = es_utils.post_request(url, value)
            result = result['hits']['hits']
            for re in result:
                if re['_source']['lat'] == 0.0 or re['_source']['lng'] == 0.0:
                    continue
                pa = [0,0,0,0]  # 0省 1市 2省,市 3UUID
                # 逆向地理位置
                geoLocal = l_g.geocoder(re['_source']['lat'],re['_source']['lng'])
                pa[0] = geoLocal[0]
                pa[1] = geoLocal[1]
                pa[2] = pa[0] + "," + pa[1]
                pa[3] = re['_source']['uuid']
                loca = [0,0,0]  # 0经纬度(,) 1省 2市
                loca[0] = str(re['_source']['lat']) + "," + str(re['_source']['lng'])
                loca[1] = pa[0]
                loca[2] = pa[1]
                local_index.append(loca)
                res_index.append(pa)
            offset = offset + 20
        return res_index,local_index
    except Exception,e:
        print e




