# -*- coding: UTF-8 -*-


from plus_vdong.all_table_compute.data_compute.plus_shop_realtime_data_compute import DbShopRealtimeDataCompute, \
    EsShopRealtimeDataCompute
from plus_vdong.common.static import public_args as p_a



class DbShopRealtimeData(object):
    '''商品实时统计信息'''
    # mysql表名 只是备注
    table_name = 'plus_shop_realtime_data'

    # 列名                  COMMENT
    # id
    # uniacid                商品id
    # type            商品销售额
    # city       商品访问人数
    # goods_sum         商品付款人数
    # new_goods_sum                商品转化率
    # visit_goods_sum        访问商品个数量
    # visit_goods_member_sum 商品访客数量
    # visit_goods_show_sum   商品浏览量
    # total                 商品销售量
    # pay_person_sum        支付人数
    # visit_person_sum      浏览人数
    # sale_prices           销售额（支付）
    # pay_order_sum         支付订单数
    # visit_sum             访问次数
    # new_member_sum        新增消费人数

    i_col = ['id', 'uniacid', 'type', 'city', 'goods_sum', 'new_goods_sum', 'visit_goods_sum','visit_goods_member_sum','visit_goods_show_sum','total',"pay_person_sum","visit_person_sum","sale_prices","pay_order_sum","visit_sum","new_member_sum"]

    def __init__(self,uniacid,type,date):
        self.__insert_data = {}
        self.data_i = {}
        self.comute = DbShopRealtimeDataCompute(uniacid, type,date)
        self.es_comute = EsShopRealtimeDataCompute(str(uniacid),date,str(type))

    def set_data(self):
        # 这里后期需要优化，有关不是当天的
        self.__insert_data["goods_sum"] = self.comute.get_goods_num()
        self.__insert_data["new_goods_sum"] = self.comute.get_new_goods_sum()
        self.__insert_data["visit_goods_sum"] = self.es_comute.get_visit_goods_sum()
        self.__insert_data["visit_goods_member_sum"] = self.es_comute.get_visit_goods_member_sum()
        self.__insert_data["visit_goods_show_sum"] = self.es_comute.get_visit_goods_show_sum()
        self.__insert_data["total"] = self.comute.get_total()
        self.__insert_data["pay_person_sum"] = self.comute.get_pay_person_sum()
        self.__insert_data["visit_person_sum"] = self.es_comute.get_visit_person_sum()
        self.__insert_data["sale_prices"] = self.comute.get_sale_prices()
        self.__insert_data["pay_order_sum"] = self.comute.get_pay_order_sum()
        self.__insert_data["visit_sum"] = self.es_comute.get_visit_sum()
        self.__insert_data["new_member_sum"] = self.comute.get_new_member_sum()
        self.__insert_data["uniacid"] = self.comute.uniacid
        self.__insert_data["type"] = self.comute.type


    def c_get_data(self):
        self.set_data()
        return self.__insert_data

    def set_data_i(self):

        self.data_i = self.c_get_data()

    def get_data(self):
        try:
            self.set_data()
            return self.__insert_data
        except Exception, e:
            p_a.logger.getLogger().error('error %s' % str(e))
