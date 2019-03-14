# -*- coding: UTF-8 -*-
# 公众号关注相关信息表
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusWechatsMemberAnalysis as p_m
class PlusWechatsMemberAnalysis(object):
    def __init__(self):
        self._table = p_m
        pass

    #获取指定日期的数据
    def get_data(self,create_date,uniacid,field):
        try:
            p =  self._table.select().where(( self._table.create_date == create_date) & ( self._table.uniacid == uniacid)).get()
            return p.__dict__.get("__data__").get(field)
        except Exception,f:
            return 0

    #获取指定日期的关注数
    def get_cumulate_user(self,uniacids,create_date,plus_versions = 1):

        data = self._table().select(self._table.uniacid).order_by(self._table.cumulate_user.desc()).where((self._table.uniacid.in_(uniacids)) & (self._table.create_date == create_date)).dicts()
        result = [];
        rank = 1;
        for item in data:
            item['rank'] = rank
            item['plus_versions'] = plus_versions
            result.append(item)
            rank = rank+1
            uniacids.remove(item["uniacid"])
        for uniacid in uniacids:

            other = {}
            other['rank'] = rank
            other['plus_versions'] = plus_versions
            other['uniacid'] = uniacid
            result.append(other)
            rank = rank + 1
        return result