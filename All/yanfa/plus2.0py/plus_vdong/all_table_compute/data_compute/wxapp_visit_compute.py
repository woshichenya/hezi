# -*- coding: UTF-8 -*-

from plus_vdong.all_table_compute.data_source.wx_source.applet_api_result import AppletApiResult

class DbWxappVisitComputer(object):

    def __init__(self,date,key,secret):
        self.result = AppletApiResult(key,secret)
        self.date = date

    def get_result(self):
        visit_data = self.result.applet_view_data(self.date)
        over_view = self.result.applet_visit_data(self.date)
        return visit_data,over_view