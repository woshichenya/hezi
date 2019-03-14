# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.db_source.middle_realtime_shop_goods import MiddleRealtimeShopGoodsSource as m_g
from  plus_vdong.all_table_compute.data_source.db_source.middle_realtime_shop_order import PlusMiddleRealtimeShopOrderSource as p_o
from plus_vdong.all_table_compute.data_source.db_source.middle_realtime_shop_order_goods import MiddleRealtimeShopOrderGoodsSource as m_o
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order import PlusMiddleShopOrderSource as s_o
from plus_vdong.all_table_compute.data_source.db_source.plus_shop_goods_info import MysqlPlusShopGoodsInfo as p_g
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a

class DbShopRealtimeDataCompute(object):
    def __init__(self,uniacid,type,date):

        self.uniacid = uniacid
        self.type = type
        if (type == 2):
            """公众号访问"""
            self.visit_way = 0
        else:
            """小程序访问"""
            self.visit_way = 1
        self.create_date = date
        # 当然临时数据表
        self.good_obj = m_g()
        # 商品表
        self.old_goods_obj = p_g();
        self.order_obj = p_o()
        self.order_goods_obj = m_o()
        self.shop_order = s_o()


    #获取支付人数
    def get_pay_person_sum(self):
        return self.order_obj.get_pay_person_sum(self.uniacid, self.visit_way, self.create_date)

    #销售额（支付）
    def get_sale_prices(self):
        return self.order_obj.get_sale_prices(self.uniacid, self.visit_way, self.create_date)

    #支付订单数
    def get_pay_order_sum(self):
        return self.order_obj.get_pay_order_sum(self.uniacid, self.visit_way, self.create_date)

    def get_new_member_sum(self):
        return self.shop_order.get_someday_new_pay_member(self.uniacid,self.type,self.create_date)

    # 获取销售商品数量
    def get_total(self):
        return self.order_goods_obj.get_total(self.uniacid, self.visit_way, self.create_date)

    # 获取商品数量
    def get_goods_num(self):
        num = self.old_goods_obj.count_goods_num(self.uniacid)
        return num
    def get_new_goods_sum(self):
        num = self.good_obj.count_date_goods_num(self.uniacid,self.create_date)
        return num

class EsShopRealtimeDataCompute(object):

    index_name_page = p_a.index_dict["applet"][0]

    def __init__(self, uniacid, day, type):
        self.app_key = str(type) + '-' + uniacid
        self.query_date = day
        # type 1代表小程序   2代表公众号
        self.type = type

    def get_visit_goods_sum(self):
        '''获取访问商品数量'''
        if self.type == 1:
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date, "currentPage", query={"query": {
                "constant_score": {"filter": {"term": {"currentPage.keyword": {"value": "pages/goods/detail/index"}}},
                                   "boost": 1.2}}}),
        elif self.type == 2 :
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date,
                                                        "c_r", query={"query": {"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}}})
        return 0

    def get_visit_goods_member_sum(self):
        '''商品访客数量'''
        if self.type == 1:
            return g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date,"openId", query={"constant_score":{"filter":{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}},"boost":1.2}}),
        elif self.type == 2 :
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date,
                                                               "openId", query={"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}})

        return 0

    def get_visit_goods_show_sum(self):
        '''商品浏览量'''
        if self.type == 1:
            return g_t.condition_count(self.app_key,self.index_name_page, self.query_date, query={"query":{"constant_score":{"filter":{"term":{"currentPage.keyword":{"value":"pages/goods/detail/index"}}},"boost":1.2}}})
        elif self.type == 2 :
            return g_t.condition_count(self.app_key, self.index_name_page, self.query_date, query={
                    "query": {"constant_score": {
                        "filter": {"term": {"c_r.keyword": {"value": "goods.detail"}}},
                        "boost": 1.2}}})

        return 0

    def get_visit_person_sum(self):
        '''获取访问人数'''
        if self.type == 1:
            return g_t.count(self.app_key,self.index_name_page, self.query_date)
        elif self.type == 2 :
            return g_t.count(self.app_key,self.index_name_page, self.query_date)
        return 0

    def get_visit_sum(self):
        '''获取访问次数'''
        if self.type == 1:
            return g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date,"openId")
        elif self.type == 2 :
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date, "openId")
        return 0

    def get_new_member_sum(self):
        '''新增消费人数'''
        if self.type == 1:
            return g_t.uniqueness_count(self.app_key,self.index_name_page, self.query_date,"openId")
        elif self.type == 2 :
            return g_t.uniqueness_count(self.app_key, self.index_name_page, self.query_date, "openId")
        return 0