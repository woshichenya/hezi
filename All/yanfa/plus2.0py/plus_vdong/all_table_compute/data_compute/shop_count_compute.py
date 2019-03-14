# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_source.db_source.shop_sale_visits import PlusShopSaleVisitSource

class DbPlusShopCountComputer(object):


    def __init__(self, uniacid,type,date ):
        self.history_data = PlusShopSaleVisitSource().get_history_data(uniacid,type)
        if self.history_data is None:
            self.history_data = DefaultValue()


    def sale_prices(self):
        return self.history_data.sale_prices

    def pay_order_sum(self):
        return self.history_data.pay_order_sum


    def pay_person_sum(self):
        return self.history_data.pay_person_sum


    def visit_sum(self):
        return self.history_data.visit_sum


    def visit_person_sum(self):
        return self.history_data.visit_person_sum


class DefaultValue(object):
    visit_person_sum = 0
    visit_sum = 0
    pay_person_sum=0
    sale_prices=0.00
    pay_order_sum=0