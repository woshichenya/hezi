# -*- coding: UTF-8 -*-

from calculate.controller.plus_shop_sale_visit import PlusShopSaleVisit as SaleVisitComputer
from data_stats.tableModel.db_base_model import PlusShopSalevisit
from data_stats.utils import query_all_wxapp,insert,query_all_wechats
from data_stats.utils import get_date_by_datetime
import sys
sys.path.append("..")


def start(arg_date):
    wxapps = query_all_wxapp()
    app_list = []
    for item in wxapps:
        model = SaleVisitComputer(item.uniacid,arg_day)
        data  = model.get_result()
        data['type'] = 1
        data['create_date'] = arg_date
        list.append(data)
    insert(PlusShopSalevisit,list)
    
    wechats = query_all_wechats()
    wechats_list = []
    for item in wechats:
        model = SaleVisitComputer(item.uniacid,arg_day)
        data  = model.get_result()
        data['type'] = 1
        data['create_date'] = arg_date
        wechats_list.append(data)
    insert(PlusShopSalevisit,wechats_list)



if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = get_date_by_datetime(1)

    start(arg_day)