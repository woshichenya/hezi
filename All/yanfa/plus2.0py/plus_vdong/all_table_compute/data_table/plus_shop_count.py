# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.shop_count_compute import DbPlusShopCountComputer
from plus_vdong.utils.date_utils import system_time_befor
class DbPlusShopCount(object):

    _result = {'uniacid':0,'sale_prices':0.00,'pay_order_sum':0,'pay_person_sum':0,'visit_sum':0,'type':1,'visit_person_sum':0}

    def __init__(self, uniacid,type):
        self._data=[]
        self.uniacid = uniacid
        self.type = type
        self.shopCountComputer = DbPlusShopCountComputer(uniacid, type, system_time_befor(-1))

    def set_data(self):
        self._result['uniacid'] = self.uniacid
        self._result['type']    = self.type
        self._result['sale_prices'] = self.shopCountComputer.sale_prices()
        self._result['pay_order_sum'] = self.shopCountComputer.pay_order_sum()
        self._result['pay_person_sum'] = self.shopCountComputer.pay_person_sum()
        self._result['visit_sum'] = self.shopCountComputer.visit_sum()
        self._result['visit_person_sum'] = self.shopCountComputer.visit_person_sum()
        self._data.append(self._result)
    def get_data(self):
        self.set_data()
        return self._data



