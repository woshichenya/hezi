# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_table.plus_shop_info_rank import DbShopInfoRank
from plus_vdong.all_table_compute.data_table.plus_wechats_info import DbPlusWechatsInfo
from plus_vdong.utils.db_util import update_by_type_uniacid,update_by_plus_versions_uniacid
from plus_vdong.tableModel.db_base_model import PlusShopInfo
from plus_vdong.tableModel.db_base_model import PlusWechatsInfo
class DbUpdateVipcnBase(object):
    def __init__(self, uniacid=None, date=None, key=None, sercet=None):
        self.uniacid = uniacid
        self.date = date
        self.key = key
        self.sercet = sercet

class DbUpdateVipcn(DbUpdateVipcnBase):
    def rank_by_shop_Info_rank(self,user,date):
        data = DbShopInfoRank().col_rank(user,date)
        # 更新数据
        update_by_type_uniacid(PlusShopInfo, data)
        return
    # 计算公众号排行
    def rand_by_wechats_info(self,users,create_date):
        data = DbPlusWechatsInfo().col_rank(users,create_date)
        # 更新数据
        update_by_plus_versions_uniacid(PlusWechatsInfo, data)
        return

