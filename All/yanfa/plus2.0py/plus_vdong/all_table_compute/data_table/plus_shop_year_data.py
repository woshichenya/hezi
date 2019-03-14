# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.shop_year_data_compute import DbPlusShopYearDataComputer
from plus_vdong.utils.date_utils import get_date_by_datetime
class DbPlusShopYearData(object):

    _result = {'uniacid':0,'sale_prices':0.00,'new_member_sum':0,'pay_person_sum':0,'type':1,'create_date':'0000'}

    def __init__(self, uniacid,type):
        self._data = []
        self._result['uniacid'] = uniacid
        self._result['type'] = type
        self.PlusShopYearDataComputer = DbPlusShopYearDataComputer(uniacid, type, get_date_by_datetime(1))

    def set_data(self):
        self._result['create_date'] = self.PlusShopYearDataComputer.get_year()
        self._result['sale_prices'] = self.PlusShopYearDataComputer.sale_prices()
        self._result['new_member_sum'] = self.PlusShopYearDataComputer.new_member_sum()
        self._result['pay_person_sum'] = self.PlusShopYearDataComputer.pay_person_sum()
        self._result['create_date'] = self.PlusShopYearDataComputer.get_year()

        self._data = [self._result]

    def get_data(self):
        self.set_data()
        return self._data