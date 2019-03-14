# -*- coding: UTF-8 -*-

from plus_vdong.common.static import public_args as p_a
from plus_vdong.all_table_compute.data_compute.wechats_article_read_count_compute import DbPlusWechatsArticleReadCountCompute
class DbPlusWechatsArticleReadCount(object):
    '''图文阅读渠道及阅读数量人数'''
    # mysql表名
    table_name = 'plus_wechats_article_read_channel'

    # 列名                        COMMENT
    # id
    # uniacid
    # share_user                 分享的人数
    # share_count                分享的次数
    # add_to_fav_user            收藏的人数
    # add_to_fav_count           收藏的次数
    # int_page_read_user         图文页（点击群发图文卡片进入的页面）的阅读人数
    # int_page_read_count        图文页的阅读次数
    # ori_page_read_user         原文页（点击图文页“阅读原文”进入的页面）的阅读人数
    # ori_page_read_count        原文页的阅读次数
    # send_article_count          每日发送文章数量
    # compare                     昨日相关比
    # create_date                创建日期

    compare = """{"add_to_fav_count_tongbi": "--", "ori_page_read_count_tongbi": "--", "ori_page_read_count_huanbi": "--", "int_page_read_count_tongbi": "--", "int_page_read_count_huanbi": "--", "add_to_fav_count_huanbi": "--", "share_count_tongbi": "--", "share_count_huanbi": "--"}"""
    i_col = { 'uniacid':"","share_user":0,"share_count":0,"add_to_fav_user":0,"add_to_fav_count":0, 'int_page_read_user':0, 'int_page_read_count':0, 'ori_page_read_user':0, 'ori_page_read_count':0,'send_article_count':0,"compare":"", 'create_date':""}
    data_i = []

    def __init__(self,uniacid,date,key,sercet):
        self.i_col["uniacid"] = uniacid
        self.i_col["create_date"] = date
        self.i_col["compare"] = self.compare
        self.comute = DbPlusWechatsArticleReadCountCompute(uniacid,date,key,sercet)
        pass
    def set_data_i(self):
         data = self.comute.get_data()
         if not data:
            data = self.i_col
         self.data_i = data
    def get_data(self):
         try:
           self.set_data_i()
         except Exception, e:
            self.data_i = self.i_col
            p_a.logger.getLogger().error('error %s' % str(e))
         return self.data_i
