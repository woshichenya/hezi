# -*- coding: UTF-8 -*-
# 公众号信息表
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusWechatsInfo
class MysqlPlusWechatsInfo(object):
    def __init__(self):
        self._table = PlusWechatsInfo
        pass

    def get_all_uniacid(self):
        data  = self._table().select(self._table.uniacid).dicts()
        uniacids = []
        for item in data:
            uniacids.append(item["uniacid"])
        return uniacids

    def get_uniacids_by_users(self,users):
        data = self._table().select(self._table.uniacid).where((self._table.user.in_(users)) & (self._table.status == 1)).dicts()
        uniacids = []
        for item in data:
            uniacids.append(item["uniacid"])
        return uniacids