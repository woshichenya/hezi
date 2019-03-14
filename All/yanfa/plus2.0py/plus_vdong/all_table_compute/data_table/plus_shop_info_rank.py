# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_compute.shop_info_rank_compute import DbShopInfoRankCompute
class DbShopInfoRank(object):
    # 更新rank gzh_rank xcx_rank排名
    def col_rank(self,user,date):
        return DbShopInfoRankCompute().get_data(user, date)
