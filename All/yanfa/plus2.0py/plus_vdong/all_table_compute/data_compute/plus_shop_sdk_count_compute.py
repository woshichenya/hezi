# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a
from plus_vdong.utils import date_utils
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order import PlusMiddleShopOrderSource

class EsPlusShopSdkCountCompute(object):

    index_name_page = p_a.index_dict["applet"][0]

    def __init__(self, uniacid, day, type):
        self.app_key = str(type) + '-' +  str(uniacid)
        self.day = day
        # type 1代表小程序   2代表公众号
        self.type =type

    def first_sum(self):
        '''首页'''
        query = {}
        if self.type == 1 :
            query = {"query":{"bool":{"must":[{"term":{"currentPage.keyword":{"value":"pages/index/index"}}}]}},"size":0}
        elif self.type == 2 :
            query = {"query":{"bool":{"must_not":[{"exists":{"field":"c_r"}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def first_order_sum(self):
        '''首页到确认订单数量'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"lastPage.keyword":{"value":"pages/index/index"}}},{"term":{"currentPage.keyword":{"value":"pages/order/pay/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must_not":[{"exists":{"field":"l_r"}}],"must":[{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def good_list_sum(self):
        '''商品列表页'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"currentPage.keyword":{"value":"pages/goods/index/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"c_r.keyword":{"value":"goods"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def good_list_order_sum(self):
        '''商品列表页到确认订单数量'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"lastPage.keyword":{"value":"pages/goods/index/index"}}},{"term":{"currentPage.keyword":{"value":"pages/order/pay/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"l_r.keyword":{"value":"goods"}}},{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def shopping_sum(self):
        '''购物车页面'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"currentPage.keyword":{"value":"pages/member/cart/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"c_r.keyword":{"value":"member.cart"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def shopping_order_sum(self):
        '''购物车页面到确认订单数量'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"lastPage.keyword":{"value":"pages/member/cart/index"}}},{"term":{"currentPage.keyword":{"value":"pages/order/pay/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"l_r.keyword":{"value":"member.cart"}}},{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def item_sum(self):
        '''商品详情页'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"c_r.keyword":{"value":"goods.detail"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def item_order_sum(self):
        '''商品详情页到确认订单数量'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must":[{"term":{"lastPage.keyword":{"value":"pages/goods/detail/index"}}},{"term":{"currentPage.keyword":{"value":"pages/order/pay/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"l_r.keyword":{"value":"goods.detail"}}},{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def other(self):
        '''其他页'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must_not":[{"terms":{"currentPage.keyword":["pages/index/index","pages/member/cart/index","pages/goods/index/index","pages/goods/detail/index"]}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must_not":[{"terms":{"l_r.keyword":["goods.detail","member.cart","goods"]}}],"must":[{"exists":{"field":"l_r"}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def other_order_sum(self):
        '''其他页到确认订单数量'''
        query = {}
        if self.type == 1:
            query = {"query":{"bool":{"must_not":[{"terms":{"lastPage.keyword":["pages/index/index","pages/member/cart/index","pages/goods/index/index","pages/goods/detail/index"]}}],"must":[{"term":{"currentPage.keyword":{"value":"pages/order/pay/index"}}}]}},"size":0}
        elif self.type == 2:
            query = {"query":{"bool":{"must_not":[{"terms":{"l_r.keyword":["goods.detail","member.cart","goods"]}}],"must":[{"exists":{"field":"l_r"}},{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def order_sum(self):
        '''确认订单'''
        query = {}
        if self.type == 1:
            query = None
        elif self.type == 2:
            query = {"query":{"bool":{"must":[{"term":{"c_r.keyword":{"value":"order.pay"}}}]}},"size":0}
        res = g_t.es_post(self.app_key, self.index_name_page, self.day, value=query)
        if res is None:
            return 0
        return res['hits']['total']

    def visit_person_sum(self):
        '''访客人数'''
        if self.type == 1:
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.day, 'openId')
        elif self.type == 2:
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.day, 'openId')


class DbPlusShopSdkCountCompute(object):
    def __init__(self, uniacid, day,type):
        self.app_key = uniacid
        self.day = day
        self.type = type
        self.db_plusMiddleShopOrderSource = PlusMiddleShopOrderSource()

    def order_pay_sum(self):
        '''支付成功'''
        return self.db_plusMiddleShopOrderSource.get_date_pay_order_sum(self.app_key,self.day,self.type)


    def visit_order_sum(self):
        '''访客下单人数'''
        return self.db_plusMiddleShopOrderSource.get_date_order_person(self.app_key,self.day,self.type)


    def visit_pay_sum(self):
        '''付款人数'''
        return self.db_plusMiddleShopOrderSource.get_date_pay_person(self.app_key,self.day,self.type)


    def order_exit(self):
        '''直接退出'''
        return self.db_plusMiddleShopOrderSource.get_unpay_order_num(self.app_key,self.day,self.type)

    def order_other(self):
        '''其他'''
        return self.db_plusMiddleShopOrderSource.get_cancel_order_num(self.app_key,self.day,self.type)