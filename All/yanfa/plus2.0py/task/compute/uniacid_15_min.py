# -*- coding: UTF-8 -*-
#每15分钟执行一次,在php项目中的etl\sh\kettle_15min.sh执行完之后
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))));
from plus_vdong.utils.date_utils import system_time_befor
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wechat_insert import DbInsertVipcn
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wxapp_insert import DbInsertApplet
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_info import MysqlPlusWechatsInfo
from plus_vdong.all_table_compute.data_source.db_source.plus_wxapp_info import MysqlPlusWxappInfo
from plus_vdong.common.static import public_args as p_a

def start(arg_day):

    os.system("sh %s/kettle_15min.sh "%(p_a.etl_sh_path))

    gzh_uniacid = MysqlPlusWechatsInfo().get_all_uniacid()
    xcx_uniacid = MysqlPlusWxappInfo().get_all_uniacid()


    for uniacid in gzh_uniacid:

        DbInsertVipcn(uniacid=uniacid,date=arg_day).shop_realtime_data()

    for uniacid in xcx_uniacid:
        DbInsertApplet(uniacid=uniacid,date=arg_day).shop_realtime_data()


if __name__ == "__main__":

    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = system_time_befor()

    start(arg_day)


