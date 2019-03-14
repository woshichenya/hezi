# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
from plus_vdong.utils.date_utils import get_date_by_datetime
from plus_vdong.compute_result_handle.db_handle.db_insert.db_wechat_insert import DbInsertVipcn


from calculate.mysql.plus_shop_info import MysqlPlusShopInfo
from  calculate.mysql.plus_users import MysqlPlusUsers
def start():

    key = 'wx7a9feb43846c1ce6'
    secret = 'a5e4858c580eb4572e7c0cf0c0aded85'
    uniacid = 1


    date = get_date_by_datetime(1)
    vipcn = DbInsertVipcn( uniacid, date, key, secret)

    vipcn.plus_wechats_member_analysis()
    pass











if __name__ == "__main__":
    start()

