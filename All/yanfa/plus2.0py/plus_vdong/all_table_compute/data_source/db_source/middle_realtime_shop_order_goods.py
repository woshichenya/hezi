# -*- coding: UTF-8 -*-
# 商品访问记录，销售等信息
import sys
sys.path.append("..")
from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopGoods
class MiddleRealtimeShopOrderGoodsSource(object):
    def __init__(self):
        self._table = PlusMiddleShopGoods
        self._db_table = "plus_middle_shop_order_goods"
        pass
    def get_total(self, uniacid,visit_way,query_date):
        sql = "select ifnull(sum(total),0) as total from %s where uniacid = '%s' and pay_date = '%s' and visit_way = %s"%(self._db_table,uniacid,query_date,visit_way)
       
        data = self._table.raw(sql).dicts()

        return data[0]["total"]