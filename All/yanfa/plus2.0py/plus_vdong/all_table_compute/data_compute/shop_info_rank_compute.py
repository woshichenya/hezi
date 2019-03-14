# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.db_source.plus_shop_info import PlusShopInfoSource
class DbShopInfoRankCompute(object):
    def __init__(self):

       self.update_data = []
       self.uniacids = []
       pass

    def get_data(self,users,yesterday):

        """全平台排序"""
        group_shop_rank = self.get_shop_rank(users,yesterday)
        rank_data = self.group_calculate_rank(group_shop_rank)
        """小程序相同类型排序"""
        xcx_rank_data = self.calculate_rank(group_shop_rank,1)
        """公众号相同类型排序"""
        gzh_rank_data = self.calculate_rank(group_shop_rank, 2)

        """所有排序写入更新数组里面"""
        for item in rank_data:

            if item["type"] == 1:
                xcx = xcx_rank_data.get(item["uniacid"],{})
                if xcx:
                    item["xcx_rank"] = xcx.get("rank",0)
                    item["gzh_rank"] = 0
            else:
                gzh = gzh_rank_data.get(item["uniacid"], {})
                if gzh:
                    item["gzh_rank"] = gzh.get("rank", 0)
                    item["xcx_rank"] = 0

            self.update_data.append(item)

        return self.update_data
    """计算公众号小程序类型排行"""
    def calculate_rank(self,data,type):
        pdata = {}
        rank = 0
        for i in data:
            if type != i["type"] : continue
            rank = rank + 1
            item = {"uniacid": i["uniacid"], "rank": rank,"type":i["type"]}
            pdata.setdefault(i["uniacid"],{})
            pdata[i["uniacid"]] = item
        return pdata
    """计算全平台排序"""
    def group_calculate_rank(self,data):
        pdata = []
        rank = 0
        for i in data:
            rank = rank + 1
            item = {"uniacid": i["uniacid"], "rank": rank,"type":i["type"]}
            pdata.append(item)
        return pdata

    """获取排名数据"""
    def get_shop_rank(self, users, create_date):

        data = PlusShopInfoSource().get_group_rank(users, create_date)
        return data

