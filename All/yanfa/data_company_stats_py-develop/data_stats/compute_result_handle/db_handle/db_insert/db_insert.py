# -*- coding: UTF-8 -*-
from data_stats.utils.db_util import insert,update_by_type_uniacid
from data_stats.all_table_compute.data_table.plus_shop_realtime_data import DbShopRealtimeData
from data_stats.all_table_compute.data_table.plus_shop_count import DbPlusShopCount
from data_stats.all_table_compute.data_table.plus_shop_year_data import DbPlusShopYearData
from data_stats.all_table_compute.data_table.plus_shop_sale_visit import DbPlusShopSaleVisit
from data_stats.all_table_compute.data_table.plus_province_sale import DbPlusProvinceSale
from data_stats.all_table_compute.data_table.plus_shop_sdk_count import DbPlusShopSdkCount
from data_stats.all_table_compute.data_table.plus_goods_sale_visit import DbGoodsSaleVisit
from data_stats.all_table_compute.data_table.plus_shop_sale_count_hour import DbPlusShopSaleCountHour

from data_stats.common.static import public_args as p_a
from data_stats.tableModel.db_base_model import *

class DbInsertBase(object):

    def __init__(self,uniacid=None,date=None,key=None,secret=None):
        self.uniacid = uniacid
        self.date = date
        self.key = key
        self.secret = secret

    def insert_province_sale(self):
        '''省份销售分布表'''
        try:
            data = DbPlusProvinceSale(self.uniacid,self.type,self.date).get_data()
            if data:
                insert(PlusProvinceSales,data)
        except Exception, e:
            p_a.logger.getLogger().error('省份销售分布表 异常：%s', e)

    def insert_shop_count(self):
        '''店铺销售总计表'''
        try:
            data = DbPlusShopCount(self.uniacid, self.type).get_data()
            if data:
                insert(PlusShopCount,data)
        except Exception, e:
            p_a.logger.getLogger().error('店铺销售总计表 异常：%s', e)


    def insert_shop_year_data(self):
        '''店铺年销售数据表'''
        try:
            data = DbPlusShopYearData(self.uniacid, self.type).get_data()
            if data:
                insert(PlusShopYearData,data)
        except Exception, e:
            p_a.logger.getLogger().error('店铺年销售数据表 异常：%s', e)

    def insert_shop_sale_visit(self):
        '''店铺销售数据'''
        try:
            data = DbPlusShopSaleVisit(self.uniacid,self.date,self.type).get_data()
            if data:
                insert(PlusShopSalevisit,data)
        except Exception, e:
            p_a.logger.getLogger().error('店铺销售数据 异常：%s', e)

    def insert_shop_sdk_count(self):
        '''店铺sdk数据'''
        try:
            data = DbPlusShopSdkCount(self.uniacid,self.type,self.date).get_data()
            if data:
                insert(PlusShopSdkCount,data)
        except Exception, e:
            p_a.logger.getLogger().error('店铺sdk数据 异常：%s', e)

    def insert_shop_sale_count_hour(self):
        '''店铺小時数据'''
        try:
            data = DbPlusShopSaleCountHour(self.uniacid, self.type).get_data()
            if data:
                insert(PlusShopSaleCountHour, data)
        except Exception, e:
            p_a.logger.getLogger().error('店铺小时计算数据 异常：%s', e)

    def goods_sale_visit(self):
        ''' 插入商品访问记录表'''
        data = DbGoodsSaleVisit(self.uniacid,self.type,self.date).get_data()
        if data:
            insert(PlusShopGoodsSalevisit,data)

    def shop_realtime_data(self):
        ''' 店铺实时数据抓取'''

        data = DbShopRealtimeData(self.uniacid, self.type,self.date).get_data()
        # if insert_or_update == 1:
        if data:
            insert(PlusShopRealtimeData, [data])
        # else:
        #     update_by_type_uniacid(PlusShopRealtimeData, [data])
        # pass

    def insert_shop_data_day(self):
        self.insert_shop_sale_visit()
        self.insert_shop_sdk_count()
        self.goods_sale_visit()
        self.insert_shop_year_data() #放insert_shop_sale_visit后
        self.insert_shop_count() #放insert_shop_sale_visit后


    def insert_hour(self):
        self.insert_province_sale()
        self.insert_shop_sale_count_hour()