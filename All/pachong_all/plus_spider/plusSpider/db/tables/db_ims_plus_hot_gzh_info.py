# -*- coding: UTF-8 -*-
# *******************************************************************************************
# **  创 建 者: tangyongchun
# **  创建日期: 2018-11-13
#
# **  文件名称：db_ims_plus_hot_gzh_info.py
# **  功能描述：实现插入、更新功能
# **
# ********************************************************************************************


from plusSpider.db.tableModel.db_base_model import ImsPlusHotGzhInfo
from plusSpider.db.utils import db_util


class VdImsPlusHotGzhInfo(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def insert_gzh_info(self):
        """ 插入公众号信息 """
        try:
            data = self.data_source
            gzh_biz = data['gzh_biz']
            create_time = data['create_time']
            if self.select_gzh(gzh_biz, create_time) == 0:
                db_util.insert(ImsPlusHotGzhInfo, [data])
            else:
                info = db_util.ImsPlusHotGzhInfo
                info.update(gzh_title=data['gzh_title'], read_sum=data['read_sum'], top_read_sum=data['top_read_sum'],
                            agree_sum=data['agree_sum'], top_agree_sum=data['top_agree_sum'],
                            send_read_sum=data['send_read_sum']) \
                    .where(info.gzh_biz == gzh_biz, info.create_time == create_time).execute()
        except Exception as e:
            print 'VdImsPlusHotGzhInfo 插入公众号信息异常', e

    def update_gzh_info(self):
        """ 更新公众号信息 """
        try:
            data_source = self.data_source
            gzh_biz = data_source['gzh_biz']
            create_time = data_source['create_time']
            if self.select_gzh(gzh_biz, create_time) == 0:
                db_util.insert(ImsPlusHotGzhInfo, [data_source])
            else:
                info = db_util.ImsPlusHotGzhInfo
                info.update(ranking=data_source['ranking']) \
                    .where(info.gzh_biz == gzh_biz, info.create_time == create_time).execute()
        except Exception as e:
            print 'VdImsPlusHotGzhInfo 更新公众号信息异常', e

    def select_gzh(self, gzh_biz, create_time):
        """ 查询公众号信息 """
        try:
            gzh = db_util.ImsPlusHotGzhInfo
            gzh_list = gzh.select().where(gzh.gzh_biz == gzh_biz, gzh.create_time == create_time)
            return len(gzh_list)
        except Exception as e:
            print 'VdImsPlusHotGzh 查询公众号数据异常', e
