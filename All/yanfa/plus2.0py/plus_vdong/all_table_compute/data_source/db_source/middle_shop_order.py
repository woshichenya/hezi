# -*- coding: UTF-8 -*-

from plus_vdong.tableModel.off_db_base_model import PlusMiddleShopOrder


class PlusMiddleShopOrderSource(object):

    def __init__(self):
        self._table = PlusMiddleShopOrder

    def select_order_data(self, uniacid, query_date, type):
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.create_date == query_date) & (self._table.type == type))

    def select_pay_data(self, uniacid, query_date, type):
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.pay_date == query_date) & (self._table.is_pay == 1) & (
                        self._table.type == type))

    def get_date_pay_order_sum(self, uniacid, query_date, type):
        '''获取指定日期的成功支付订单'''
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.is_pay == 1) & (self._table.pay_date == query_date) & (
                        self._table.type == type)).count()

    def get_date_order_sum(self, uniacid, query_date, type):
        '''获取指定日期的所有订单(包括未支付)'''
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.create_date == query_date) & (
                        self._table.type == type)).count()

    def get_date_order_person(self, uniacid, query_date, type):
        '''获取某天的下单人数'''
        try:
            sql = "SELECT \
                        COUNT(DISTINCT openid, openid) as num \
                    FROM \
                        plus_middle_shop_order \
                    WHERE  uniacid = %d  \
                    AND create_date = '%s' and type = %d" % (int(uniacid), query_date, type)
            res = self._table().raw(sql)
            return res[0].num
        except Exception:
            return 0

    def get_date_pay_person(self, uniacid, query_date, type):
        '''获取某天的支付人数'''
        try:
            sql = "SELECT \
                        COUNT(DISTINCT openid, openid) as num \
                    FROM \
                        plus_middle_shop_order \
                    WHERE is_pay = 1 \
                    AND uniacid = %d  \
                    AND pay_date = '%s' and type = %d" % (int(uniacid), query_date, type)
            res = self._table().raw(sql)
            return res[0].num
        except Exception:
            return 0

    def get_cancel_order_num(self, uniacid, query_date, type):
        '''获取某天的取消訂單數'''
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.create_date == query_date) & (self._table.is_pay == -1) & (
                        self._table.type == type)).count()

    def get_unpay_order_num(self, uniacid, query_date, type):
        '''获取某天的未支付訂單數'''
        return self._table().select().where(
            (self._table.uniacid == uniacid) & (self._table.create_date == query_date) & (self._table.is_pay == 0) & (
                        self._table.type == type)).count()

    def get_hour_sale_prices(self, uniacid, query_date, type, hour):
        try:
            sql = "SELECT \
                                ifnull(SUM(pay_price) ,0) as pay_price \
                            FROM \
                                plus_middle_shop_order \
                            WHERE is_pay = 1 \
                            AND uniacid = %d  \
                            AND pay_date = '%s' and type = %d and `hour` = %d " % (int(uniacid), query_date, type,int(hour))
            res = self._table().raw(sql)
            return res[0].pay_price
        except Exception as e:
            return 0

    def get_year_new_pay_member(self, uniacid, type,year):
        try:
            sql = "SELECT COUNT(DISTINCT openid, openid) as num\
            FROM plus_middle_shop_order WHERE openid NOT IN ( \
            SELECT \
                DISTINCT openid \
            FROM \
                plus_middle_shop_order \
            where YEAR(pay_date) < Year(NOW()) \
                and uniacid = %d and  type =%d) \
                  and uniacid = %d and type = %d and is_pay = 1" % (int(uniacid), type, int(uniacid), type)
            res = self._table().raw(sql)
            return res[0].num
        except Exception as e:
            return 0


    def get_someday_new_pay_member(self, uniacid, type,query_date):
        try:
            sql = "SELECT COUNT(DISTINCT openid, openid) as num\
            FROM plus_middle_shop_order WHERE openid NOT IN ( \
            SELECT DISTINCT \
                DISTINCT openid \
            FROM \
                plus_middle_shop_order \
            where create_date < '%s' \
                and uniacid = %d and  type =%d) \
                  and uniacid = %d and type = %d and create_date = '%s' and is_pay = 1" % (query_date,int(uniacid), type, int(uniacid), type,query_date)
            res = self._table().raw(sql)
            return res[0].num
        except Exception as e:
            return 0

    def get_year_pay_person_sum(self, uniacid, type,year):
        try:
            sql = "SELECT COUNT(DISTINCT openid, openid) as num\
            FROM plus_middle_shop_order WHERE \
                  uniacid = %d and type = %d  and is_pay = 1 and YEAR(pay_date) = '%s'" % (int(uniacid), type,year)
            res = self._table().raw(sql)
            return res[0].num
        except Exception as e:
            return 0

    def get_year_sale_prices(self, uniacid, type,year):
        try:
            sql = "SELECT ifnull(SUM(pay_price),0) as pay_price\
            FROM plus_middle_shop_order WHERE \
                  uniacid = %d and type = %d  and is_pay = 1 and YEAR(pay_date) = '%s'" % (int(uniacid), type,year)
            res = self._table().raw(sql).get()
            return res.pay_price
        except Exception as e:
            return 0