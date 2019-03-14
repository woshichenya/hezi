# -*- coding: UTF-8 -*-

from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopGoods


class MiddleRealtimeShopGoodsSource(object):

    def __init__(self):
        self.Model = PlusMiddleShopGoods
    def count_goods_num(self,uniacid):
        num = self.Model().select(self.Model.goodsid).where((self.Model.uniacid == uniacid) & (self.Model.deleted == 0)).count()
        return num


    def count_date_goods_num(self,uniacid,query_date):
        num = self.Model().select(self.Model.goodsid).where((self.Model.uniacid == uniacid) & (self.Model.deleted == 0) & (self.Model.create_date == query_date)).count()

        return num