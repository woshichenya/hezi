# -*- coding: UTF-8 -*-

import sys
from data_stats.all_table_compute.data_table.data_user_stats import DataUserStats
from data_stats.all_table_compute.data_table.data_weichen_module_stats import DataWeichenModuleStats

sys.path.append("..")
import time


def start(arg_date):
    pass


if __name__ == "__main__":
    #res = AppletApiResult('wx83735ca894a2bd5a','7c12705434003aab06fbb8a2f057999d')
    #print res.applet_visit_data(get_date_by_datetime(1))
    #print res.applet_view_data(get_date_by_datetime(1))
    #list = DataUserStats('2019-2-25').get_data()
    #print list
    list = DataWeichenModuleStats('2019-2-25').get_data()
    print list