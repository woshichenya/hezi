# -*- coding: UTF-8 -*-
# 店铺信息表

from plus_vdong.tableModel.db_base_model import *
from plus_vdong.tableModel.db_base_model import PlusShopInfo
from plus_vdong.tableModel.db_base_model import PlusShopSalevisit
class PlusShopInfoSource(object):
    def __init__(self):
        self._table = PlusShopInfo
        self._sale = PlusShopSalevisit
    def get_group_rank(self,user,create_date):
        user_str_list = [str(x) for x in user]
        sql = """select i.uniacid,i.type,ifnull(s.sale_prices,0) as  sale_prices from plus_shop_info as i
				left join plus_shop_sale_visit as s on i.uniacid = s.uniacid and i.type = s.type and  s.create_date = "{create_date}"
				 where i.user_id in ({users}) order by sale_prices desc
              """
        sql = sql.format(create_date=create_date,users=",".join(user_str_list))
        data = database.execute_sql(sql)
        pdata = []
        for item in data:
           pdata.append({"uniacid":item[0],"type":item[1],"sale_prices":item[2]})
        return pdata

