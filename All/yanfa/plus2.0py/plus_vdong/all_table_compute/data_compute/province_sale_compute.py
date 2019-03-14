# -*- coding: UTF-8 -*-


from plus_vdong.utils.date_utils import system_time_befor
from plus_vdong.all_table_compute.data_source.db_source.middle_realtime_shop_order import PlusMiddleRealtimeShopOrderSource
from plus_vdong.all_table_compute.data_source.es_source import general_template as g_t
from plus_vdong.common.static import public_args as p_a
import datetime


class DbPlusProvinceSaleComputer(object):

    def __init__(self,uniacid,date,type):
        self.date = date
        self.uniacid = uniacid
        self.type = type
        self.PlusMiddleRealtimeShopOrderSource = PlusMiddleRealtimeShopOrderSource()

    def get_province_sale_and_pay_person(self):
        return self.PlusMiddleRealtimeShopOrderSource.select_province_sale(self.uniacid,self.date, self.type)


class EsPlusProvinceSaleComputer(object):

    index_name_page = p_a.index_dict["applet"][0]

    def __init__(self, uniacid, date, type):
        if isinstance(date, (datetime.datetime, datetime.date)):
            self.date = date
        else:
            self.date = system_time_befor(1)
        self.app_key = str(type) + '-' + uniacid
        # type 1代表小程序   2代表公众号
        self.type = type

    def visit_person_sum(self):
        ''' 访客数 '''
        if self.type == 1:
            return g_t.terms_aggs(self.app_key, self.index_name_page, self.date, 'ufo.province')
        elif self.type == 2:
            return g_t.terms_aggs(self.app_key, self.index_name_page, self.date, 'province')
        return None

