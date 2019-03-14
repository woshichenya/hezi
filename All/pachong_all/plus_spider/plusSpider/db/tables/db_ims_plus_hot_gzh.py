# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：db_ims_plus_hot_gzh.py
# **  功能描述：实现插入、更新功能
# **
# ********************************************************************************************

from plusSpider.db.tableModel.db_base_model import ImsPlusHotGzh
from plusSpider.db.utils import db_util


class VdImsPlusHotGzh(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def insert_gzh(self):
        """ 插入公众号数据 """
        try:
            gzh_info = self.data_source
            if self.select_gzh(gzh_info['biz'], None) == 0:
                db_util.insert(ImsPlusHotGzh, [gzh_info])
            else:
                gzh = db_util.ImsPlusHotGzh
                gzh.update(uin_hao=gzh_info['uin_hao'], logo=gzh_info['logo'], title=gzh_info['title'],
                           auth=gzh_info['auth'], qr_code_url=gzh_info['qr_code_url'],
                           new_send_time=gzh_info['new_send_time']) \
                    .where(gzh.biz == gzh_info['biz']).execute()
        except Exception as e:
            print 'VdImsPlusHotGzh 插入公众号数据异常', e

    def update_gzh(self):
        """ 更新公众号数据 """
        try:
            gzh_info = self.data_source
            if self.select_gzh(None, gzh_info['uin_hao']) == 0:
                db_util.insert(ImsPlusHotGzh, [gzh_info])
            else:
                gzh = db_util.ImsPlusHotGzh
                gzh.update(remark=gzh_info['remark'], send_article_sum=gzh_info['send_article_sum'],
                           average_send_article=gzh_info['average_send_article'],
                           average_top_read=gzh_info['average_top_read'],
                           average_nottop_read=gzh_info['average_nottop_read'],
                           average_top_agree=gzh_info['average_top_agree'], max_read_sum=gzh_info['max_read_sum']) \
                    .where(gzh.uin_hao == gzh_info['uin_hao']).execute()
        except Exception as e:
            print 'VdImsPlusHotGzh 更新公众号数据异常', e

    def select_gzh(self, biz, uin_hao):
        """ 查询公众号信息 """
        gzh_list = 0
        try:
            gzh = db_util.ImsPlusHotGzh
            if biz is not None:
                gzh_list = gzh.select().where(gzh.biz == biz)
            elif uin_hao is not None:
                gzh_list = gzh.select().where(gzh.uin_hao == uin_hao)
            return len(gzh_list)
        except Exception as e:
            print 'VdImsPlusHotGzh 查询公众号数据异常', e

    def select_gzh_all(self):
        """ 查询所有公众号信息 """
        try:
            gzh = db_util.ImsPlusHotGzh
            return gzh.select(gzh.biz, gzh.uin_hao, gzh.title)
        except Exception as e:
            print 'VdImsPlusHotGzh 查询所有公众号信息数据异常', e
