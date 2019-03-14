# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.middle_user import DataMiddleUserSource
from data_stats.all_table_compute.data_source.db_source.user_new_keep import DataUserNewKeepSource

from data_stats.utils.date_utils import get_date_ymd

import time, datetime

class DataUserNewKeepCompute(object):

    def __init__(self,query_date):
        self.query_date = query_date
        timeArray = time.strptime(self.query_date, "%Y-%m-%d")
        self.timeStamp = int(time.mktime(timeArray))

    def new_user(self):
        return DataMiddleUserSource().count_user_from_reg_date(self.query_date)

    def next_save_user(self):
        query_date = get_date_ymd(self.timeStamp - 86400)
        date_info = DataUserNewKeepSource().get_info_someday(query_date)
        if date_info is None:
            return None
        else:
            date_info['next_save_user'] =  DataUserNewKeepSource().count_new_user_active_someday(query_date,self.query_date)

    def third_save_user(self):
        query_date = get_date_ymd(self.timeStamp - (3*86400))
        date_info = DataUserNewKeepSource().get_info_someday(query_date)
        if date_info is None:
            return None
        else:
            date_info['third_save_user'] =  DataUserNewKeepSource().count_new_user_active_someday(query_date,self.query_date)

    def seventh_save_user(self):
        query_date = get_date_ymd(self.timeStamp - (7*86400))
        date_info = DataUserNewKeepSource().get_info_someday(query_date)
        if date_info is None:
            return None
        else:
            date_info['seventh_save_user'] =  DataUserNewKeepSource().count_new_user_active_someday(query_date,self.query_date)

    def thirtieth_save_user(self):
        query_date = get_date_ymd(self.timeStamp - (30*86400))
        date_info = DataUserNewKeepSource().get_info_someday(query_date)
        if date_info is None:
            return None
        else:
            date_info['thirtieth_save_user'] =  DataUserNewKeepSource().count_new_user_active_someday(query_date,self.query_date)
        return date_info