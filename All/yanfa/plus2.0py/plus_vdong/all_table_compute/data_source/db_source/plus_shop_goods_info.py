# -*- coding: UTF-8 -*-
# 商品访问记录，销售等信息
import sys
sys.path.append("..")
from plus_vdong.tableModel.db_base_model import PlusShopGoodsInfo
class MysqlPlusShopGoodsInfo(object):
    def __init__(self):
        self._table = PlusShopGoodsInfo
        pass

    def get_all_good_id(self,uniacid):
        data  = self._table().select(self._table.good,self._table.uniacid).where(self._table.uniacid == uniacid).dicts()
        good_ids = []
        for item in data:
            good_ids.append(item)
        return good_ids

    def count_goods_num(self,uniacid):
        num = self._table().select(self._table.good).where((self._table.uniacid == uniacid) & (self._table.status == 1)).count()
        return num