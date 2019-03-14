# -*- coding: UTF-8 -*-

from plus_vdong.common.static import public_args as p_a
from plus_vdong.all_table_compute.data_compute.wechats_article_read_channel_compute import DbPlusWechatsArticleReadChannelCompute
class DbPlusWechatsArticleReadChannel(object):
    '''图文阅读渠道及阅读数量人数'''
    # mysql表名
    table_name = 'plus_wechats_article_read_channel'

    # 列名                        COMMENT
    # id
    # uniacid
    # int_page_read_user         图文页（点击群发图文卡片进入的页面）的阅读人数
    # int_page_read_count        图文页的阅读次数
    # ori_page_read_user         原文页（点击图文页“阅读原文”进入的页面）的阅读人数
    # ori_page_read_count        原文页的阅读次数
    # user_source
    # create_date                创建日期

    i_col = { 'uniacid':"", 'int_page_read_user':0, 'int_page_read_count':0, 'ori_page_read_user':0, 'ori_page_read_count':0,'user_source':0, 'create_date':""}
    data_i = []

    def __init__(self,uniacid,date,key,sercet):
        self.i_col["uniacid"] = uniacid
        self.i_col["create_date"] = date


        self.comute = DbPlusWechatsArticleReadChannelCompute(uniacid,date,key,sercet)
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
