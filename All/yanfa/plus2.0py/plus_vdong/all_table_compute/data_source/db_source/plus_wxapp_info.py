# -*- coding: UTF-8 -*-
# 小程序信息表
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusWxappInfo
class MysqlPlusWxappInfo(object):
    def __init__(self):
        self._table = PlusWxappInfo
        pass

    def get_all_uniacid(self):
        data  = self._table().select(self._table.uniacid).dicts()
        uniacids = []
        for item in data:
            uniacids.append(item["uniacid"])
        return uniacids

