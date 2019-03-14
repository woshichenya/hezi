# -*- coding: UTF-8 -*-
import sys


sys.path.append("..")
from plus_vdong.common.static import public_args as p_a
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.utils import es_utils


class AppletInit(object):
    index_name_user = p_a.index_dict["applet"][3]
    index_name_page = p_a.index_dict["applet"][0]

    def __init__(self, app_key, day, type):
        self.app_key = str(type) + '-' + app_key
        print self.app_key
        self.day = day
        self.type = type

    def get_user_list(self, req_json):
        today_users = []
        if req_json:
            for user in req_json["aggregations"]["NAME"]["buckets"]:
                today_users.append(user["key"])
        return today_users

    def get_query_history(self,size_json):
        history_users = []
        hits = size_json["hits"]["hits"]
        for i in range(0, len(hits)):
            history_users += hits[i]["_source"]["new_user_list"]
        return history_users

    def get_user_history(self,app_key, name ):
        """ 查找历史用户 """
        from_in = 0
        size_in = 50
        history_users = []
        # 查询小于self.day 的历史用户
        query_in = {"bool":{"must_not":[{"range":{"day":{"gte":self.day}}}]}}
        _json = g_t.page_query(app_key, name, 'all', _from=from_in, size=size_in,query=query_in)
        if _json is not None:
            history_users += self.get_query_history(_json)
            total_hits = _json["hits"]["total"]
            for i in range(0, total_hits / size_in):
                from_in += size_in
                history_users += self.get_query_history(
                    g_t.page_query(app_key, name, 'all', _from=from_in, size=size_in,query=query_in))
        return history_users

    def user_init(self):
        """  初始化用户索引 """
        # 创建user别名
        g_t.add_alias(self.app_key, self.index_name_page, self.day)
        # 获取当天活跃用户
        today_json = g_t.terms_aggs(self.app_key, self.index_name_page, self.day, "uuid")
        active_user_list = self.get_user_list(today_json)
        # 获取历史用户列表
        history_users = self.get_user_history(self.app_key,self.index_name_page)
        # 新用户列表
        active_user_list = set(active_user_list)
        history_users = set(history_users)
        new_user_list = active_user_list - history_users
        # 定义doc元数据信息
        user_doc_id = {"index": {"_id": self.day}}
        # 定义doc数据信息
        user_doc = {
            "new_user_num": len(new_user_list),
            "new_user_list": list(new_user_list),
            "active_user_num": len(active_user_list),
            "active_user_list": list(active_user_list),
            "history_user_num": len(history_users),
            "history_user_list": list(history_users),
            "day": self.day
        }
        index = "logstash-%s-%s-all" % (self.app_key, self.index_name_user)
        # index es
        es_utils.es_bulk(index, [user_doc_id, user_doc])
        # 刷新索引
        g_t.refresh(self.app_key, self.index_name_user, self.day)

    def init(self):
        try:
            self.user_init()
        except Exception, e:
            p_a.logger.getLogger().error('applet_init error %s' % str(e))

