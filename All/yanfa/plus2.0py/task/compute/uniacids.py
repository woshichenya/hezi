# -*- coding: UTF-8 -*-
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from plus_vdong.all_table_compute.data_compute_brefor_init.es_init import AppletInit
from plus_vdong.compute_result_handle.db_handle.db_update.db_update import DbUpdate
from plus_vdong.utils.date_utils import system_time_befor
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wechat_insert import DbInsertVipcn
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wxapp_insert import DbInsertApplet
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_info import MysqlPlusWechatsInfo
from plus_vdong.all_table_compute.data_source.db_source.plus_wxapp_info import MysqlPlusWxappInfo
from plus_vdong.common.static import public_args as p_a
import user_group

def start(arg_day):
    os.system("sh %s/kettle.sh "%(p_a.etl_sh_path))

    gzh_uniacid = MysqlPlusWechatsInfo().get_all_uniacid()
    xcx_uniacid = MysqlPlusWxappInfo().get_all_uniacid()

    """公众号循环"""
    for uniacid in gzh_uniacid:
        try:
            AppletInit(str(uniacid),arg_day, str(2)).init()
            DbInsertVipcn(uniacid=str(uniacid),date=arg_day).insert_shop_data_day()
        except Exception,f:
            print f
            pass

    """小程序循环"""
    for uniacid in xcx_uniacid:
        try:
            # 初始化小程序相关数据
            AppletInit(str(uniacid), arg_day, '1').init()
            DbInsertApplet(uniacid=str(uniacid), date=arg_day).insert_shop_data_day()
            DbUpdate(str(uniacid), arg_day, '1').update_game_all()
        except Exception,f:
            pass
if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = system_time_befor(-1)

    start(arg_day)

    # # # 当数据执行完成后，在执行排名
    user_group.start(arg_day)
