# -*- coding: UTF-8 -*-

from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopOrder


class PlusMiddleRealtimeShopOrderSource(object):

    def __init__(self):
        self._table = PlusMiddleShopOrder
        self._db_table = "plus_middle_shop_order"

    def select_order_data(self, uniacid, query_date):
        return self._table().select().where((self._table.uniacid == uniacid) & (self._table.create_date == query_date) & (self._table.status >0))


    # 获取店铺订单支付数量
    def get_pay_order_sum(self, uniacid,visit_way, query_date):
        sql = "select count(*) as count from %s where uniacid = '%s' and pay_date = '%s' and visit_way = %s and is_pay = 1"%(self._db_table,uniacid,query_date,visit_way)
        data = self._table.raw(sql).dicts()
        for item in data:
            return item["count"]
        return 0


    # 获取店铺订单销售额
    def get_sale_prices(self, uniacid,visit_way, query_date):
        sql = "select ifnull(sum(pay_price),0) as pay_price from %s where uniacid = '%s' and pay_date = '%s' and visit_way = %s and is_pay = 1" % (self._db_table, uniacid, query_date, visit_way)
        data = self._table.raw(sql).dicts()
        for item in data:
            return item["pay_price"]
        return 0

    # 获取订单支付人数
    def get_pay_person_sum(self, uniacid,visit_way, query_date):
        sql = "select count(distinct openid) as count from %s where uniacid = '%s' and pay_date = '%s' and visit_way = %s and is_pay = 1" % (self._db_table, uniacid, query_date, visit_way)
        data = self._table.raw(sql).dicts()
        for item in data:
            return item["count"]
        return 0

    def select_province_sale(self, uniacid, query_date,type):
        uniacid = int(uniacid)
        sql = 'SELECT \
            SUM(plus_middle_shop_order.pay_price) as sale_prices, \
            COUNT(DISTINCT plus_middle_shop_member.openid,plus_middle_shop_member.openid) as pay_person_sum, \
            plus_middle_shop_member.province \
            FROM \
            plus_middle_shop_order \
            LEFT JOIN plus_middle_shop_member ON plus_middle_shop_order.uniacid = plus_middle_shop_member.uniacid \
            AND plus_middle_shop_order.openid = plus_middle_shop_member.openid \
            WHERE \
            plus_middle_shop_order.uniacid =%d \
            AND \
            plus_middle_shop_order.pay_date=\'%s\' \
            AND \
            plus_middle_shop_order.is_pay = 1 \
            AND plus_middle_shop_order.type =%d \
            group by plus_middle_shop_member.province' % (int(uniacid), query_date,type)
        return self._table().raw(sql)

