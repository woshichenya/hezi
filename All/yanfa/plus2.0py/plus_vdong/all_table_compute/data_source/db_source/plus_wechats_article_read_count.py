# -*- coding: UTF-8 -*-
# 公众号文章阅读相关信息表
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusWechatsArticleReadCount as p_r_c
class PlusWechatsArticleReadCount(object):
    def __init__(self):
        self._table = p_r_c
        pass

    #获取指定日期的数据
    def get_data(self,create_date,uniacid,field):
        try:
            p =  self._table.select().where(( self._table.create_date == create_date) & ( self._table.uniacid == uniacid)).get()
            return p.__dict__.get("__data__").get(field)
        except Exception,f:
            return 0

