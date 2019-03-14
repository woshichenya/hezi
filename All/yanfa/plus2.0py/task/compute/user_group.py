# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))));
from plus_vdong.utils.date_utils import system_time_befor
from plus_vdong.compute_result_handle.db_handle.db_update.db_wechat_update import DbUpdateVipcn
from  plus_vdong.all_table_compute.data_source.db_source.plus_users import MysqlPlusUsers

def start(arg_day):


    vipcn = DbUpdateVipcn()
    # 获取以分组为下标多个user_id为值
    data = MysqlPlusUsers().get_group_data()
    for group, users in data.items():
        vipcn.rank_by_shop_Info_rank(users,arg_day)
        vipcn.rand_by_wechats_info(users,arg_day)





if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = system_time_befor(-1)

    start(arg_day)

