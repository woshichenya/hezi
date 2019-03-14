# -*- coding: UTF-8 -*-

from plus_vdong.common.wechat.wechat import Wechat
from plus_vdong.common.wechat.api.app.datacube import DataCube

class AppletApiResult(object):

    def __init__(self,key,secret):
        wechat = Wechat(key,secret)
        self.api = DataCube(wechat)

    def applet_visit_data(self,data_date):
        return self.api.get_analysis_daily_visit_trend(data_date,data_date)

    def applet_view_data(self,data_date):
        return self.api.get_analysis_daily_summary(data_date,data_date)
