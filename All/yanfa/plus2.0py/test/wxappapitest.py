# -*- coding: UTF-8 -*-

from controller.wxapp.wxapp_visit import WxappVisit
from plus_vdong.tableModel.db_base_model import PlusWxappVisit
from plus_vdong.utils import query_all_wxapp,insert
from plus_vdong.utils import get_date_by_datetime
import sys
sys.path.append("..")


def start(arg_date):
    wxapps = query_all_wxapp()
    list = [] # TODO
    for item in wxapps:
        model = WxappVisit(item.key,item.secret,item.uniacid)
        data  = model.get_data(arg_date)
        list.append(data)
    insert(PlusWxappVisit,list)



if __name__ == "__main__":
    try:
        arg_day = sys.argv[1]
    except IndexError, e:
        arg_day = get_date_by_datetime(1)

    start(arg_day)

