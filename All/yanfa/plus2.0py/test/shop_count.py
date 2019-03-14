# -*- coding: UTF-8 -*-

import sys
from plus_vdong.all_table_compute.data_source.wx_source.applet_api_result import AppletApiResult
from plus_vdong.utils.date_utils import get_date_by_datetime
sys.path.append("..")
import time


def start(arg_date):
    pass


if __name__ == "__main__":
    #res = AppletApiResult('wx83735ca894a2bd5a','7c12705434003aab06fbb8a2f057999d')
    #print res.applet_visit_data(get_date_by_datetime(1))
    #print res.applet_view_data(get_date_by_datetime(1))
    ts = int(time.time())
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))