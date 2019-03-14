# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.db_source.plus_shop_goods_info import MysqlPlusShopGoodsInfo
from plus_vdong.all_table_compute.data_source.db_source.middle_shop_order_goods import MiddleShopOrderGoods
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a

# TODO 为进行es与db隔离
class DbGoodsSaleVisitCompute(object):

    index_name_page = p_a.index_dict["applet"][0]

    def __init__(self,uniacid,type,create_date):

       self.__insert_data = []
       self.uniacid = uniacid
       self.type = type
       self.create_date = create_date
       self.mysql_goods_info = MysqlPlusShopGoodsInfo()
       self.middle_shop_order_goods = MiddleShopOrderGoods()


    def get_all_rows(self):

        good_ids = self.__get_all_good_id()

        for item in good_ids:
            self.__circulation(item["good"],item["uniacid"],self.create_date,self.type)
        return self.__insert_data

    """获取所有商品"""
    def __get_all_good_id(self):
        data =  self.mysql_goods_info.get_all_good_id(self.uniacid)
        return data

    """循环每个商品计算"""
    def __circulation(self,good_id,uniacid,create_date,type):
        item = {}
        if (type == 2):
            """公众号访问"""
            visit_way = 0
        else:
            """小程序访问"""
            visit_way = 1

        data = self.middle_shop_order_goods.get_pay_good_order(good_id, uniacid,create_date,visit_way)

        """商品单日销售额"""
        sales_price = self.__get_sales_price(data,visit_way)
        """商品单日付款人数"""
        total_num = self.__get_total_num(data,visit_way)
        """商品销售数量"""
        pay_person_sum = self.__get_pay_person_sum(data,visit_way)
        visit_person_sum = self.__get_visit_person_sum(good_id,uniacid,create_date,type)
        try:
            good_lv = pay_person_sum / visit_person_sum
        except Exception :
            good_lv = 0

        item.update({"type": type, "uniacid": uniacid, "good": good_id, "visit_person_sum": 0,"create_date":create_date})
        item["sales_price"] = sales_price
        item["pay_person_sum"] = pay_person_sum
        item["total"] = total_num
        item["visit_person_sum"] = visit_person_sum
        item["good_lv"] = good_lv

        self.__insert_data.append(item)


    """获取商品单日销售额"""
    """
        visit_way = 访问方式 0公众号 1小程序
    """
    def __get_sales_price(self,data,visit_way):
        sales_price = 0
        for item in data:
            if item["visit_way"] == visit_way:
                    sales_price += item["pay_price"]
        return sales_price

    """商品单日付款人数"""
    """
       visit_way = 访问方式 0公众号 1小程序
    """
    def __get_pay_person_sum(self,data,visit_way):
        member = set()
        for item in data:
            if item["visit_way"] == visit_way:
                member.add(item["openid"])

        return len(member)

    """商品销售数量"""
    def __get_total_num(self,data,visit_way):
        total_num = 0
        for item in data:
            if item["visit_way"] == visit_way:
                total_num += item["total"]

        return total_num

    '''
            获取访问人数
            param 
                good_id 商品id
                uniacid 商城唯一值
                create_date 日期
                type 类型 1小程序店铺 2公众号店铺
        '''
    def __get_visit_person_sum(self,good_id,uniacid,create_date,type):
        """商品单日访问人数"""
        query = {}
        if self.type == 1 :
            query = {"query": {"bool": {"must": [{"term": {"ag.id.keyword": {"value": good_id}}}]}}, "size": 0}
        elif self.type == 2 :
            query = {"query": {"bool": {"must": [{"term": {"c_id.keyword": {"value": good_id}}}]}},"size": 0}
        res = g_t.es_post(str(self.type) + '-' + self.uniacid, self.index_name_page, self.create_date, value=query)
        if res is None:
            return 0
        return res['hits']['total']


