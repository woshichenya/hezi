# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_compute.shop_sale_visit_compute import DbPlusShopSaleVisitComputer, \
    EsPlusShopSaleVisitComputer


class DbPlusShopSaleVisit(object):
    _result = {
        'uniacid': 0, 'type': 1, 'visit_sum': 0, 'visit_person_sum': 0, 'goods_sum': 0, 'new_goods_sum': 0,
        'visit_goods_sum': 0,
        'visit_goods_member_sum': 0, 'visit_goods_show_sum': 0,
        'order_sum': 0, 'order_prices': 0, 'order_person_sum': 0, 'pay_order_sum': 0, 'pay_person_sum': 0,
        'sale_prices': 0, 'new_member_sum': 0, 'new_member_prices_sum': 0,
        'old_member_sum': 0, 'old_member_prices_sum': 0, 'visit_order_lv': 0.00, 'order_pay_lv': 0.00,
        'visit_pay_lv': 0.00
    }

    def __init__(self, uniacid, date, type):
        self._data = []
        self._result['uniacid'] = uniacid
        self._result['type'] = type
        self._result['create_date'] = date
        self.date = date
        self.db_PlusShopSaleVisitComputer = DbPlusShopSaleVisitComputer(uniacid, date,type)
        self.es_PlusShopSaleVisitComputer = EsPlusShopSaleVisitComputer(str(uniacid), date,str(type))

    def set_data(self):

        pay_result = self.db_PlusShopSaleVisitComputer.parse_pay_data()
        self._result = dict(self._result, **pay_result)
        order_result = self.db_PlusShopSaleVisitComputer.parse_order_data()
        self._result = dict(self._result, **order_result)
        good_result = self.db_PlusShopSaleVisitComputer.parse_goods_data()
        self._result = dict(self._result, **good_result)
        good_visit_result = self.es_PlusShopSaleVisitComputer.parse_goods_visit_data()
        self._result = dict(self._result, **good_visit_result)
        order_rate = self.db_PlusShopSaleVisitComputer.parse_order_rate(self._result['visit_person_sum'],
                                                                self._result['order_person_sum'],
                                                                self._result['pay_person_sum'])
        self._result = dict(self._result, **order_rate)
        self._data.append(self._result)

    def get_data(self):
        self.set_data()
        return self._data
