# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_info import MysqlPlusWechatsInfo
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_member_analysis import PlusWechatsMemberAnalysis
from plus_vdong.common.static import public_args as p_a

class DbWechatsInfoCompute(object):
    def __init__(self,users,create_date):
        self.users = users
        self.create_date = create_date

    def get_rank(self):
        uniacids = MysqlPlusWechatsInfo().get_uniacids_by_users(self.users)
        data = PlusWechatsMemberAnalysis().get_cumulate_user(uniacids,self.create_date)
        return data
