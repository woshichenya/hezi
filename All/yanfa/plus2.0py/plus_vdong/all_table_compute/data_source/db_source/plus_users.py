# -*- coding: UTF-8 -*-
# 店铺信息表
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusUsers
class MysqlPlusUsers(object):
    def __init__(self):
        self._table = PlusUsers
        pass

    def get_all_users(self):
        data  = self._table().select(self._table.user,self._table.group).where(self._table.status == 1).dicts()
        pdata = []
        for item in data:
            pdata.append(item)
        return pdata

    def get_group_data(self):
        group = {}
        data = self.get_all_users()
        for item in data:
            group_key = str(item["group"])
            group.setdefault(group_key,[])
            group[group_key].append(item["user"])
        return group
