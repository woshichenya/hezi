# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_source.db_source.shop_sale_visits import PlusShopSaleVisitSource
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order import PlusMiddleShopOrderSource
from plus_vdong.all_table_compute.data_source.db_source.shop_year_data import PlusShopYearDataSource

class DbPlusShopYearDataComputer(object):

    def __init__(self,uniacid,type,date):
        self.uniacid = uniacid
        self.type = type
        self.year = date.strftime('%Y')
        self.yearData = PlusShopSaleVisitSource().get_year_data(uniacid,type,self.year)
        if self.yearData is None:
            self.yearData = DefaultValue()


    def sale_prices(self):
        return PlusMiddleShopOrderSource().get_year_sale_prices(self.uniacid,self.type,self.year)

    def pay_person_sum(self):
        return PlusMiddleShopOrderSource().get_year_pay_person_sum(self.uniacid,self.type,self.year)

    def new_member_sum(self):
        return PlusMiddleShopOrderSource().get_year_new_pay_member(self.uniacid,self.type,self.year)

    def get_year(self):
        return self.year

class DefaultValue(object):
    sale_prices = 0.00
    pay_person_sum = 0
    new_member_sum = 0

