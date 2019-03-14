# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))));
from data_stats.utils.date_utils import system_time_befor
from data_stats.compute_result_handle.db_handle.db_insert.db_wechat_insert import DbInsertVipcn
from data_stats.compute_result_handle.db_handle.db_insert.db_wxapp_insert import DbInsertApplet
from data_stats.all_table_compute.data_source.db_source.plus_wechats_info import MysqlPlusWechatsInfo
from data_stats.all_table_compute.data_source.db_source.plus_wxapp_info import MysqlPlusWxappInfo
import user_group
def start(arg_day):
    gzh_uniacid = MysqlPlusWechatsInfo().get_all_uniacid()
    xcx_uniacid = MysqlPlusWxappInfo().get_all_uniacid()

    """公众号循环"""
    for uniacid in gzh_uniacid:
        try:
            DbInsertVipcn(uniacid=uniacid,date=arg_day).insert_hour()
        except Exception,f:
            pass

    """小程序循环"""
    for uniacid in xcx_uniacid:
        try:
            DbInsertApplet(uniacid=uniacid, date=arg_day).insert_hour()
        except Exception,f:
            pass


    # # # 当数据执行完成后，在执行排名
    user_group.start(arg_day)
if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = system_time_befor(-1)

    start(arg_day)