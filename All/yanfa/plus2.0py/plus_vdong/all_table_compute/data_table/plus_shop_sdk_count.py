# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_compute.plus_shop_sdk_count_compute import EsPlusShopSdkCountCompute,DbPlusShopSdkCountCompute
from plus_vdong.common.api import data_format
from plus_vdong.common.static import public_args as p_a
from plus_vdong.utils import date_utils

'''
商城页面访问统计
'''
class DbPlusShopSdkCount(object):


    i_col = [
        'uniacid',
        'first_sum',           # '首页',
        'first_order_sum',     # '首页到确认订单数量',
        'good_list_sum',       # '商品列表页',
        'good_list_order_sum', # '商品列表页到确认订单数量',
        'shopping_sum',        # '购物车页面',
        'shopping_order_sum',  # '购物车页面到确认订单数量',
        'item_sum',            # '商品详情页',
        'item_order_sum',      # '商品详情页到确认订单数量',
        'other',               # '其他页',
        'other_order_sum',     # '其他页到确认订单数量',
        'order_sum',           # '确认订单',
        'order_pay_sum',       # '支付成功',
        'order_exit',          # '直接退出',
        'order_other',         # '其他',
        'visit_person_sum',           # '访客人数',
        'visit_order_sum',     # '访客下单人数',
        'visit_pay_sum',       # '付款人数',
        'create_date',         # 0000-00-00,
        'create_time',         # ,
        'type'                #
    ]

    def __init__(self,app_key, type, day):
        self.app_key = app_key
        self.day = day
        self.type = type
        self.es_plus_shop_sdk_count = EsPlusShopSdkCountCompute(self.app_key ,self.day,self.type)
        self.db_plus_shop_sdk_count = DbPlusShopSdkCountCompute(self.app_key ,self.day,type)
        # 计算后数据
        self.i_data = []

    def set_data_i(self):
        self.i_data.append(self.app_key)
        self.i_data.append(self.es_plus_shop_sdk_count.first_sum())            # 首页()),
        self.i_data.append(self.es_plus_shop_sdk_count.first_order_sum())      # 首页到确认订单数量()),
        self.i_data.append(self.es_plus_shop_sdk_count.good_list_sum())        # 商品列表页()),
        self.i_data.append(self.es_plus_shop_sdk_count.good_list_order_sum())  # 商品列表页到确认订单数量()),
        self.i_data.append(self.es_plus_shop_sdk_count.shopping_sum())         # 购物车页面()),
        self.i_data.append(self.es_plus_shop_sdk_count.shopping_order_sum())   # 购物车页面到确认订单数量()),
        self.i_data.append(self.es_plus_shop_sdk_count.item_sum())             # 商品详情页()),
        self.i_data.append(self.es_plus_shop_sdk_count.item_order_sum())       # 商品详情页到确认订单数量()),
        self.i_data.append(self.es_plus_shop_sdk_count.other())                # 其他页()),
        self.i_data.append(self.es_plus_shop_sdk_count.other_order_sum())      # 其他页到确认订单数量()),
        self.i_data.append(self.es_plus_shop_sdk_count.order_sum())            # 确认订单()),
        self.i_data.append(self.db_plus_shop_sdk_count.order_pay_sum())        # 支付成功()),
        self.i_data.append(self.db_plus_shop_sdk_count.order_exit())           # 直接退出()),
        self.i_data.append(self.db_plus_shop_sdk_count.order_other())          # 其他()),
        self.i_data.append(self.es_plus_shop_sdk_count.visit_person_sum())     # 访客人数()),
        self.i_data.append(self.db_plus_shop_sdk_count.visit_order_sum())      #  访客下单人数()),
        self.i_data.append(self.db_plus_shop_sdk_count.visit_pay_sum())        #  付款人数()),
        self.i_data.append(self.day)
        self.i_data.append(date_utils.system_time())
        self.i_data.append(self.type)

    def get_data(self):
        try:
            self.set_data_i()
        except Exception, e:
            p_a.logger.getLogger().error('error %s' % str(e))
        return data_format.list_for_dict(self.i_col, [self.i_data])

    def get_day(self):
        return self.day

    def get_app_key(self):
        return self.app_key



