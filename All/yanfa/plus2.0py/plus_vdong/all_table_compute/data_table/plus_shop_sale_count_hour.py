# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.shop_sale_hour_compute import DbPlusShopSaleCountHourComputer


class DbPlusShopSaleCountHour(object):

    _result = {
        'uniacid': 0, 'type': 1, 'create_date':'0000-00-00','hour':0,'sale_prices':0.00
    }

    def __init__(self, uniacid, type):
        self._data = []
        self._result['uniacid'] = uniacid
        self._result['type'] = type
        self.db_PlusShopSaleVisitComputer = DbPlusShopSaleCountHourComputer(uniacid,type)

    def set_data(self):
        self._result['sale_prices'] = self.db_PlusShopSaleVisitComputer.get_sale_prices()
        self._result['create_date'] = self.db_PlusShopSaleVisitComputer.get_date()
        self._result['hour'] = self.db_PlusShopSaleVisitComputer.get_hour()
        self._data.append(self._result)

    def get_data(self):
        self.set_data()
        return self._data
