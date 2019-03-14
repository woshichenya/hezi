# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_source.db_source.middle_shop_good import PlusMiddleShopGoodSource
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_member import PlusMiddleShopMemberSource
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order import PlusMiddleShopOrderSource
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a

'''计算结果'''
class DbPlusShopSaleVisitComputer(object):
    def __init__(self, uniacid, query_date ,type):
        self.query_date = query_date
        self.uniacid = uniacid
        self.type = type
        self.OrderMysql = PlusMiddleShopOrderSource()
        self.MemberMysql = PlusMiddleShopMemberSource()
        self.GoodsMysql = PlusMiddleShopGoodSource()

    def parse_pay_data(self):
        result = {'pay_order_sum': 0, 'sale_prices': 0.00, 'pay_person_sum': 0, 'new_member_sum': 0,
                  'new_member_prices_sum': 0.00, 'old_member_sum': 0, 'old_member_prices_sum': 0.00}
        new_openid = self.MemberMysql.select_query_date_openid(self.uniacid,self.query_date)
        openid = []
        new_uv = []
        old_uv = []
        for item in self.OrderMysql.select_pay_data(self.uniacid,self.query_date,self.type):
            result['pay_order_sum'] += 1 #支付订单数加1
            result['sale_prices'] += item.pay_price #支付金额累加

            '''支付人数'''
            if item.openid not in openid:
                openid.append(item.openid)
                result['pay_person_sum'] += 1  # 支付人数加1

            '''新用户支付人数 订单金额'''
            if item.openid in new_openid:
                if item.openid not in new_uv:
                    result['new_member_sum'] += 1  # 新用户支付人数加1
                    new_uv.append(item.openid)
                result['new_member_prices_sum'] += item.pay_price

            else:
                '''老用户支付人数 订单金额'''
                if item.openid not in old_uv:
                    result['old_member_sum'] += 1  # 老用户支付人数加1
                    new_uv.append(item.openid)
                result['old_member_prices_sum'] += item.pay_price
        return result


    def parse_order_data(self):
        result = {'order_sum':0,'order_prices':0.00,'order_person_sum':0}
        openid = []
        for item in self.OrderMysql.select_pay_data(self.uniacid,self.query_date,self.type):
            result['order_sum'] += 1
            result['order_prices'] += item.pay_price
            if item.openid not in openid:
                result['order_person_sum'] += 1
                openid.append(item.openid)
        return result


    def parse_goods_data(self):
        result = {'goods_sum':0,'new_goods_sum':0}
        result['goods_sum'] = self.GoodsMysql.count_goods_num(self.uniacid)
        result['new_goods_sum'] = self.GoodsMysql.count_date_goods_num(self.uniacid,self.query_date)
        return result

    def parse_order_rate(self,visit_person_sum,order_person_sum,pay_person_sum):
        result = {'visit_order_lv':0.00,'visit_pay_lv':0.00,'order_pay_lv':0.00}
        if  visit_person_sum:
            '''访问-下单转化率'''
            result['visit_order_lv'] = order_person_sum / visit_person_sum * 100
            result['visit_pay_lv'] = pay_person_sum / visit_person_sum * 100

        if  order_person_sum:
            '''下单-付款转化率'''
            result['order_pay_lv'] = pay_person_sum / order_person_sum * 100
        return result


    def get_result(self):
        return self._result


class EsPlusShopSaleVisitComputer(object):
    index_name_page = p_a.index_dict["applet"][0]
    '''计算结果'''

    def __init__(self, uniacid, query_date ,type):
        self.query_date = query_date
        self.app_key = str(type) + '-' + uniacid
        # type 1代表小程序   2代表公众号
        self.type = type

    def parse_goods_visit_data(self):
        if self.type == 1:
            return  {
                # 当日访问量
                'visit_sum': g_t.count(self.app_key,self.index_name_page, self.query_date),
                # 访问人数
                'visit_person_sum': g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date,"openId"),
                # 访问商品数量
                'visit_goods_sum': g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date, "currentPage",query={"query":{"constant_score":{"filter":{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}},"boost":1.2}}}),
                # 商品访客数量
                'visit_goods_member_sum': g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date,"openId", query={"constant_score":{"filter":{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}},"boost":1.2}}),
                # 商品浏览量
                'visit_goods_show_sum': g_t.condition_count(self.app_key,self.index_name_page, self.query_date, query={"query":{"constant_score":{"filter":{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}},"boost":1.2}}}),
            }
        elif self.type == 2:
            return {
                # 当日访问量
                'visit_sum': g_t.count(self.app_key, self.index_name_page, self.query_date),
                # 访问人数
                'visit_person_sum': g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date, "openId"),
                # 访问商品数量
                'visit_goods_sum': g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date,
                                                        "c_r", query={"query": {"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}}}),
                # 商品访客数量
                'visit_goods_member_sum': g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date,
                                                               "openId", query={"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}}),
                # 商品浏览量
                'visit_goods_show_sum': g_t.condition_count(self.app_key, self.index_name_page, self.query_date, query={
                    "query": {"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}}}),
            }
        return {}
