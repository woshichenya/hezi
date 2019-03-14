# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order import PlusMiddleShopOrderSource
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a
import time

'''计算结果'''
class DbPlusShopSaleCountHourComputer(object):
    def __init__(self, uniacid ,type):
        ts = int(time.time()) - 3600
        self.query_date = time.strftime("%Y-%m-%d", time.localtime(ts))
        self.hour = time.strftime("%H", time.localtime(ts))
        self.uniacid = uniacid
        self.type = type
        self.OrderMysql = PlusMiddleShopOrderSource()

    def get_sale_prices(self):
        return PlusMiddleShopOrderSource().get_hour_sale_prices(self.uniacid,self.query_date,self.type,self.hour)

    def get_date(self):
        return self.query_date

    def get_hour(self):
        return self.hour

