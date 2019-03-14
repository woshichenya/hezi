# -*- coding: UTF-8 -*-
# 商品访问记录，销售等信息
import sys
sys.path.append("..")
from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopOrderGoods
class MiddleShopOrderGoods(object):
    def __init__(self):
        self._table = PlusMiddleShopOrderGoods
        self._where = []
        pass
    """获取"""
    """获取订单"""
    def get_good_order(self,good_id,uniacid,create_date,visit_way):

        data = self._table().select()\
            .where((self._table.goodsid == good_id) & (self._table.uniacid == uniacid) & (self._table.create_date == create_date)&(self._table.visit_way ==visit_way))\
            .dicts()
        order_data = []

        for item in data:
            order_data.append(item)
        return order_data

    """获取支付订单"""
    def get_pay_good_order(self,good_id,uniacid,pay_date,visit_way):
        data = self._table().select()\
            .where((self._table.goodsid == good_id) & (self._table.uniacid == uniacid) & (self._table.pay_date == pay_date) &(self._table.visit_way ==visit_way))\
            .dicts()

        order_data = []
        for item in data:
            order_data.append(item)
        return order_data
